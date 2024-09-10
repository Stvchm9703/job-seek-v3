from twirp.exceptions import InvalidArgument, TwirpServerException
import twirp.errors as errors

def NotFoundError(argument):
    return TwirpServerException(
        code=errors.Errors.NotFound,
        message="cannot found the result in {}".format(argument),
        meta={"argument": argument},
    )

def UnimplementedError(argument):
    return TwirpServerException(
        code=errors.Errors.Unimplemented,
        message="{} is not implemented".format(argument),
        meta={"argument": argument},
    )