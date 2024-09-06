# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: user-management.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .. import job_search as _job_search__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class UserProfileType(betterproto.Enum):
    STUDENT = 0
    EMPLOYEE = 1
    CERTIFICATE = 2
    PART_TIME_EMPLOYEE = 3
    CONTRACT_EMPLOYEE = 4
    OTHER = 5


@dataclass(eq=False, repr=False)
class GetUserRequest(betterproto.Message):
    reference_id: Optional[str] = betterproto.string_field(
        1, optional=True, group="_reference_id"
    )
    user_id: Optional[str] = betterproto.string_field(
        2, optional=True, group="_user_id"
    )
    user_name: Optional[str] = betterproto.string_field(
        3, optional=True, group="_user_name"
    )
    user_email: Optional[str] = betterproto.string_field(
        4, optional=True, group="_user_email"
    )
    user_phone: Optional[str] = betterproto.string_field(
        5, optional=True, group="_user_phone"
    )
    user_password: Optional[str] = betterproto.string_field(
        6, optional=True, group="_user_password"
    )


@dataclass(eq=False, repr=False)
class UserResponse(betterproto.Message):
    status: str = betterproto.string_field(1)
    user_id: str = betterproto.string_field(2)
    message: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class UserAccount(betterproto.Message):
    id: str = betterproto.string_field(1)
    user_name: str = betterproto.string_field(2)
    user_password: str = betterproto.string_field(3)
    user_email: str = betterproto.string_field(4)
    user_phone: str = betterproto.string_field(5)
    user_address: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class UserCvProfile(betterproto.Message):
    user_id: str = betterproto.string_field(1)
    cv_id: str = betterproto.string_field(2)
    cv_data: bytes = betterproto.bytes_field(3)
    cv_keywords: List["PreferenceKeyword"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class UserProfile(betterproto.Message):
    id: str = betterproto.string_field(1)
    user_id: str = betterproto.string_field(2)
    title: str = betterproto.string_field(3)
    position: str = betterproto.string_field(4)
    description: str = betterproto.string_field(5)
    salary: str = betterproto.string_field(6)
    location: str = betterproto.string_field(7)
    company: str = betterproto.string_field(8)
    type: "UserProfileType" = betterproto.enum_field(9)
    keywords: List["PreferenceKeyword"] = betterproto.message_field(10)
    start_date: str = betterproto.string_field(11)
    end_date: str = betterproto.string_field(12)
    company_detail: Optional["_job_search__.CompanyDetail"] = betterproto.message_field(
        13, optional=True, group="_company_detail"
    )


@dataclass(eq=False, repr=False)
class PreferenceKeyword(betterproto.Message):
    kw_id: str = betterproto.string_field(1)
    user_id: str = betterproto.string_field(2)
    keyword: str = betterproto.string_field(3)
    value: str = betterproto.string_field(4)
    type: str = betterproto.string_field(5)
    is_positive: bool = betterproto.bool_field(6)


@dataclass(eq=False, repr=False)
class ListUserProfileResponse(betterproto.Message):
    profiles: List["UserProfile"] = betterproto.message_field(1)
    status: str = betterproto.string_field(2)
    message: str = betterproto.string_field(3)
    user_id: str = betterproto.string_field(4)


class UserManagementServiceStub(betterproto.ServiceStub):
    async def create_user_account(
        self,
        user_account: "UserAccount",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/CreateUserAccount",
            user_account,
            UserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_user_account(
        self,
        get_user_request: "GetUserRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserAccount":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/GetUserAccount",
            get_user_request,
            UserAccount,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_user_account(
        self,
        user_account: "UserAccount",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/UpdateUserAccount",
            user_account,
            UserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def create_user_profile(
        self,
        user_profile: "UserProfile",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/CreateUserProfile",
            user_profile,
            UserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_user_profile(
        self,
        user_profile: "UserProfile",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserProfile":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/GetUserProfile",
            user_profile,
            UserProfile,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def list_user_profile(
        self,
        get_user_request: "GetUserRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "ListUserProfileResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/ListUserProfile",
            get_user_request,
            ListUserProfileResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def update_user_profile(
        self,
        user_profile: "UserProfile",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/UpdateUserProfile",
            user_profile,
            UserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def delete_user_profile(
        self,
        get_user_request: "GetUserRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/DeleteUserProfile",
            get_user_request,
            UserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def import_user_profile_from_cv(
        self,
        user_cv_profile: "UserCvProfile",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/ImportUserProfileFromCV",
            user_cv_profile,
            UserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def create_user_cv_profile(
        self,
        user_cv_profile: "UserCvProfile",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserResponse":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/CreateUserCVProfile",
            user_cv_profile,
            UserResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def get_user_cv_profile(
        self,
        get_user_request: "GetUserRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "UserCvProfile":
        return await self._unary_unary(
            "/job_seek.user_management.UserManagementService/GetUserCVProfile",
            get_user_request,
            UserCvProfile,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )


class UserManagementServiceBase(ServiceBase):

    async def create_user_account(self, user_account: "UserAccount") -> "UserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_user_account(
        self, get_user_request: "GetUserRequest"
    ) -> "UserAccount":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_user_account(self, user_account: "UserAccount") -> "UserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def create_user_profile(self, user_profile: "UserProfile") -> "UserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_user_profile(self, user_profile: "UserProfile") -> "UserProfile":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list_user_profile(
        self, get_user_request: "GetUserRequest"
    ) -> "ListUserProfileResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def update_user_profile(self, user_profile: "UserProfile") -> "UserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delete_user_profile(
        self, get_user_request: "GetUserRequest"
    ) -> "UserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def import_user_profile_from_cv(
        self, user_cv_profile: "UserCvProfile"
    ) -> "UserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def create_user_cv_profile(
        self, user_cv_profile: "UserCvProfile"
    ) -> "UserResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def get_user_cv_profile(
        self, get_user_request: "GetUserRequest"
    ) -> "UserCvProfile":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_create_user_account(
        self, stream: "grpclib.server.Stream[UserAccount, UserResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_user_account(request)
        await stream.send_message(response)

    async def __rpc_get_user_account(
        self, stream: "grpclib.server.Stream[GetUserRequest, UserAccount]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_user_account(request)
        await stream.send_message(response)

    async def __rpc_update_user_account(
        self, stream: "grpclib.server.Stream[UserAccount, UserResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_user_account(request)
        await stream.send_message(response)

    async def __rpc_create_user_profile(
        self, stream: "grpclib.server.Stream[UserProfile, UserResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_user_profile(request)
        await stream.send_message(response)

    async def __rpc_get_user_profile(
        self, stream: "grpclib.server.Stream[UserProfile, UserProfile]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_user_profile(request)
        await stream.send_message(response)

    async def __rpc_list_user_profile(
        self, stream: "grpclib.server.Stream[GetUserRequest, ListUserProfileResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.list_user_profile(request)
        await stream.send_message(response)

    async def __rpc_update_user_profile(
        self, stream: "grpclib.server.Stream[UserProfile, UserResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.update_user_profile(request)
        await stream.send_message(response)

    async def __rpc_delete_user_profile(
        self, stream: "grpclib.server.Stream[GetUserRequest, UserResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.delete_user_profile(request)
        await stream.send_message(response)

    async def __rpc_import_user_profile_from_cv(
        self, stream: "grpclib.server.Stream[UserCvProfile, UserResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.import_user_profile_from_cv(request)
        await stream.send_message(response)

    async def __rpc_create_user_cv_profile(
        self, stream: "grpclib.server.Stream[UserCvProfile, UserResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.create_user_cv_profile(request)
        await stream.send_message(response)

    async def __rpc_get_user_cv_profile(
        self, stream: "grpclib.server.Stream[GetUserRequest, UserCvProfile]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get_user_cv_profile(request)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/job_seek.user_management.UserManagementService/CreateUserAccount": grpclib.const.Handler(
                self.__rpc_create_user_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                UserAccount,
                UserResponse,
            ),
            "/job_seek.user_management.UserManagementService/GetUserAccount": grpclib.const.Handler(
                self.__rpc_get_user_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetUserRequest,
                UserAccount,
            ),
            "/job_seek.user_management.UserManagementService/UpdateUserAccount": grpclib.const.Handler(
                self.__rpc_update_user_account,
                grpclib.const.Cardinality.UNARY_UNARY,
                UserAccount,
                UserResponse,
            ),
            "/job_seek.user_management.UserManagementService/CreateUserProfile": grpclib.const.Handler(
                self.__rpc_create_user_profile,
                grpclib.const.Cardinality.UNARY_UNARY,
                UserProfile,
                UserResponse,
            ),
            "/job_seek.user_management.UserManagementService/GetUserProfile": grpclib.const.Handler(
                self.__rpc_get_user_profile,
                grpclib.const.Cardinality.UNARY_UNARY,
                UserProfile,
                UserProfile,
            ),
            "/job_seek.user_management.UserManagementService/ListUserProfile": grpclib.const.Handler(
                self.__rpc_list_user_profile,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetUserRequest,
                ListUserProfileResponse,
            ),
            "/job_seek.user_management.UserManagementService/UpdateUserProfile": grpclib.const.Handler(
                self.__rpc_update_user_profile,
                grpclib.const.Cardinality.UNARY_UNARY,
                UserProfile,
                UserResponse,
            ),
            "/job_seek.user_management.UserManagementService/DeleteUserProfile": grpclib.const.Handler(
                self.__rpc_delete_user_profile,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetUserRequest,
                UserResponse,
            ),
            "/job_seek.user_management.UserManagementService/ImportUserProfileFromCV": grpclib.const.Handler(
                self.__rpc_import_user_profile_from_cv,
                grpclib.const.Cardinality.UNARY_UNARY,
                UserCvProfile,
                UserResponse,
            ),
            "/job_seek.user_management.UserManagementService/CreateUserCVProfile": grpclib.const.Handler(
                self.__rpc_create_user_cv_profile,
                grpclib.const.Cardinality.UNARY_UNARY,
                UserCvProfile,
                UserResponse,
            ),
            "/job_seek.user_management.UserManagementService/GetUserCVProfile": grpclib.const.Handler(
                self.__rpc_get_user_cv_profile,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetUserRequest,
                UserCvProfile,
            ),
        }
