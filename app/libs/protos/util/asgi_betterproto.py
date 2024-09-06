import asyncio
import base64
from collections import namedtuple
from collections.abc import AsyncIterator
import inspect
import time
from urllib.parse import quote

from async_timeout import timeout
import grpc

import grpclib
from sonora import protocol

_HandlerCallDetails = namedtuple(
    "_HandlerCallDetails", ("method", "invocation_metadata")
)


class grpcASGI(grpc.Server):
    def __init__(self, application=None):
        self._application = application
        self._handlers = []

    async def __call__(self, scope, receive, send):
        """
        Our actual ASGI request handler. Will execute the request
        if it matches a configured gRPC service path or fall through
        to the next application.
        """

        assert scope["type"] == "http"

        rpc_method = self._get_rpc_handler(scope["path"])
        request_method = scope["method"]

        if rpc_method:
            if request_method == "POST":
                context = self._create_context(scope)
                try:
                    async with timeout(context.time_remaining()):
                        await self._do_grpc_request(rpc_method, context, receive, send)
                except asyncio.TimeoutError:
                    context.code = grpc.StatusCode.DEADLINE_EXCEEDED
                    context.details = "request timed out at the server"
                    await self._do_grpc_error(context, send)

            elif request_method == "OPTIONS":
                await self._do_cors_preflight(scope, receive, send)
            else:
                await send({"type": "http.response.start", "status": 400})
                await send(
                    {"type": "http.response.body", "body": b"", "more_body": False}
                )

        elif self._application:
            await self._application(scope, receive, send)

        else:
            await send({"type": "http.response.start", "status": 404})
            await send({"type": "http.response.body", "body": b"", "more_body": False})

    def _get_rpc_handler(self, path):
        handler_call_details = _HandlerCallDetails(path, None)
        rpc_handler = None
        # print("self._handlers", type(self._handlers))
        for handler in self._handlers:
            # print("handler", handler)
            # print("handler typr", type(handler))
            # key = handler.__mapping__().get(path)
            # print("key", key)
            rpc_handler = handler.__mapping__().get(path)
            if rpc_handler:
                return rpc_handler

        return None

    def _create_context(self, scope):
        timeout = None
        metadata = []

        for header, value in scope["headers"]:
            if timeout is None and header == b"grpc-timeout":
                timeout = protocol.parse_timeout(value)
            else:
                if header.endswith(b"-bin"):
                    value = base64.b64decode(value)
                else:
                    value = value.decode("ascii")

                metadata.append((header.decode("ascii"), value))

        return ServicerContext(timeout, metadata)

    async def _do_grpc_request(self, rpc_method, context, receive, send):
        print("rpc_method", rpc_method)
        # print("rpc_method", rpc_method.request_deserializer)
        # request_proto_iterator = (
        #     rpc_method.request_deserializer(message)
        #     async for _, _, message in protocol.unwrap_message_asgi(receive)
        # )

        method = rpc_method.func
        print("context", context)
        print("receive", receive)
        print("send", send)
        # print("request_proto_iterator", request_proto_iterator)

        # if rpc_method.request_streaming:
        if (
            rpc_method.cardinality == grpclib.const.Cardinality.STREAM_STREAM
            or rpc_method.cardinality == grpclib.const.Cardinality.STREAM_UNARY
        ):
            coroutine = method(request_proto_iterator, context)
        else:
            # request_proto = await anext(request_proto_iterator)
            print("mmethod", method.__name__)
            print("mmethod", inspect.getfullargspec(method))

            coroutine = method({recv_message: lambda: None}, context)
            print("coroutine", coroutine)
        headers = [
            (b"Content-Type", b"application/grpc-web+proto"),
            (b"Access-Control-Allow-Origin", b"*"),
            (b"Access-Control-Expose-Headers", b"*"),
        ]

        try:
            if (
                rpc_method.cardinality == grpclib.const.Cardinality.STREAM_STREAM
                or rpc_method.cardinality == grpclib.const.Cardinality.UNARY_STREAM
            ):
                await self._do_streaming_response(
                    rpc_method, receive, send, context, headers, coroutine
                )
            else:
                await self._do_unary_response(
                    rpc_method, receive, send, context, headers, coroutine
                )
        except grpc.RpcError:
            await self._do_grpc_error(context, send)

    async def _do_streaming_response(
        self, rpc_method, receive, send, context, headers, coroutine
    ):
        message = await anext(coroutine)

        status = protocol.grpc_status_to_http_status(context.code)

        body = protocol.wrap_message(
            False, False, rpc_method.response_serializer(message)
        )

        if context._initial_metadata:
            headers.extend(context._initial_metadata)

        await send(
            {"type": "http.response.start", "status": status, "headers": headers}
        )

        await send({"type": "http.response.body", "body": body, "more_body": True})

        async for message in coroutine:
            body = protocol.wrap_message(
                False, False, rpc_method.response_serializer(message)
            )

            send_task = asyncio.create_task(
                send({"type": "http.response.body", "body": body, "more_body": True})
            )

            recv_task = asyncio.create_task(receive())

            done, pending = await asyncio.wait(
                {send_task, recv_task}, return_when=asyncio.FIRST_COMPLETED
            )

            if recv_task in done:
                send_task.cancel()
                result = recv_task.result()
                if result["type"] == "http.disconnect":
                    break
            else:
                recv_task.cancel()

        trailers = [("grpc-status", str(context.code.value[0]))]
        if context.details:
            trailers.append(("grpc-message", quote(context.details)))

        if context._trailing_metadata:
            trailers.extend(context._trailing_metadata)

        trailer_message = protocol.pack_trailers(trailers)
        body = protocol.wrap_message(True, False, trailer_message)
        await send({"type": "http.response.body", "body": body, "more_body": False})

    async def _do_unary_response(
        self, rpc_method, receive, send, context, headers, coroutine
    ):
        message = await coroutine

        status = protocol.grpc_status_to_http_status(context.code)
        headers.append((b"grpc-status", str(context.code.value[0]).encode()))
        if context.details:
            headers.append((b"grpc-message", quote(context.details)))

        if context._initial_metadata:
            headers.extend(context._initial_metadata)

        if message is not None:
            message_data = protocol.wrap_message(
                False, False, rpc_method.response_serializer(message)
            )
        else:
            message_data = b""

        if context._trailing_metadata:
            trailers = context._trailing_metadata
            trailer_message = protocol.pack_trailers(trailers)
            trailer_data = protocol.wrap_message(True, False, trailer_message)
        else:
            trailer_data = b""

        content_length = len(message_data) + len(trailer_data)

        headers.append((b"content-length", str(content_length).encode()))

        await send(
            {"type": "http.response.start", "status": status, "headers": headers}
        )
        await send(
            {"type": "http.response.body", "body": message_data, "more_body": True}
        )
        await send(
            {"type": "http.response.body", "body": trailer_data, "more_body": False}
        )

    async def _do_grpc_error(self, context, send):
        headers = [
            (b"Content-Type", b"application/grpc-web+proto"),
            (b"Access-Control-Allow-Origin", b"*"),
            (b"Access-Control-Expose-Headers", b"*"),
        ]

        status = protocol.grpc_status_to_http_status(context.code)
        headers.append((b"grpc-status", str(context.code.value[0]).encode()))

        if context.details:
            headers.append((b"grpc-message", quote(context.details).encode()))

        await send(
            {"type": "http.response.start", "status": status, "headers": headers}
        )
        await send({"type": "http.response.body", "body": b"", "more_body": False})

    async def _do_cors_preflight(self, scope, receive, send):
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    (b"Content-Type", b"text/plain"),
                    (b"Content-Length", b"0"),
                    (b"Access-Control-Allow-Methods", b"POST, OPTIONS"),
                    (b"Access-Control-Allow-Headers", b"*"),
                    (b"Access-Control-Allow-Origin", b"*"),
                    (b"Access-Control-Allow-Credentials", b"true"),
                    (b"Access-Control-Expose-Headers", b"*"),
                ],
            }
        )
        await send({"type": "http.response.body", "body": b"", "more_body": False})

    def add_generic_rpc_handlers(self, handlers):
        self._handlers.extend(handlers)

    def add_insecure_port(self, port):
        raise NotImplementedError()

    def add_secure_port(self, port):
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()


class ServicerContext(grpc.ServicerContext):
    def __init__(self, timeout=None, metadata=None):
        self.code = grpc.StatusCode.OK
        self.details = None

        self._timeout = timeout

        if timeout is not None:
            self._deadline = time.monotonic() + timeout
        else:
            self._deadline = None

        self._invocation_metadata = metadata or tuple()
        self._initial_metadata = None
        self._trailing_metadata = None

    def set_code(self, code):
        self.code = code

    def set_details(self, details):
        self.details = details

    async def abort(self, code, details):
        if code == grpc.StatusCode.OK:
            raise ValueError()

        self.set_code(code)
        self.set_details(details)

        raise grpc.RpcError()

    async def abort_with_status(self, status):
        if status == grpc.StatusCode.OK:
            raise ValueError()

        self.set_code(status)

        raise grpc.RpcError()

    async def send_initial_metadata(self, initial_metadata):
        self._initial_metadata = [
            (key.encode("ascii"), value.encode("ascii"))
            for key, value in protocol.encode_headers(initial_metadata)
        ]

    async def set_trailing_metadata(self, trailing_metadata):
        self._trailing_metadata = protocol.encode_headers(trailing_metadata)

    def invocation_metadata(self):
        return self._invocation_metadata

    def time_remaining(self):
        if self._deadline is not None:
            return max(self._deadline - time.monotonic(), 0)
        else:
            return None

    def peer(self):
        raise NotImplementedError()

    def peer_identities(self):
        raise NotImplementedError()

    def peer_identity_key(self):
        raise NotImplementedError()

    def auth_context(self):
        raise NotImplementedError()

    def add_callback(self):
        raise NotImplementedError()

    def cancel(self):
        raise NotImplementedError()

    def is_active(self):
        raise NotImplementedError()


# Copied from https://github.com/python/cpython/pull/8895


_NOT_PROVIDED = object()


async def anext(async_iterator, default=_NOT_PROVIDED):
    """anext(async_iterator[, default])
    Return the next item from the async iterator.
    If default is given and the iterator is exhausted,
    it is returned instead of raising StopAsyncIteration.
    """
    if not isinstance(async_iterator, AsyncIterator):
        raise TypeError(f"anext expected an AsyncIterator, got {type(async_iterator)}")
    anxt = async_iterator.__anext__
    print("anxt", anxt)
    return await anxt()

    try:
        return await anxt()
    except StopAsyncIteration:
        if default is _NOT_PROVIDED:
            raise
        return default
