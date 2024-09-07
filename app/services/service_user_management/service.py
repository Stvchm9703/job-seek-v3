from libs.twirp_protos import user_management_twirp

# from libs.protos.job_seek.user_management import UserResponse
# from libs.protos.job_seek.prediction import SurveyUserPerfenceRequest
from libs.database import init_db

# prediction_twirp._sym_db.RegisterMessage(UserResponse)
# prediction_twirp._sym_db.RegisterMessage(SurveyUserPerfenceRequest)


import sys

sys.path.append("app/libs/twirp_protos")
from user_management_pb2 import (
    UserAccount,
    UserProfile,
    UserCVProfile,
    GetUserRequest,
    ListUserProfileResponse,
    UserResponse,
)


# import prediction_twirp
from twirp.exceptions import InvalidArgument, TwirpServerException
import twirp.errors as errors
import libs.database.queries.user_account as queries


def NotFoundError(argument):
    return TwirpServerException(
        code=errors.Errors.NotFound,
        message="cannot found the result in {}".format(argument),
        meta={"argument": argument},
    )


class UserManagementService(object):
    __db_conn__ = None

    def __init__(self, **kwarg) -> None:
        pass

    async def check_db(self):
        if self.__db_conn__ is None:
            self.__db_conn__ = await init_db()
        return True

    # UserAccount
    async def CreateUserAccount(self, context, request: UserAccount) -> UserResponse:
        await self.check_db()
        try:
            result = await queries.create_user_account(self.__db_conn__, request)
            return UserResponse(
                message="created user",
                user_id=result["id"],
                status="success",
            )
        except Exception as e:
            print("Exception", e)
            raise InvalidArgument(argument="Create user account failed", error=e)

    async def GetUserAccount(self, context, request: GetUserRequest) -> UserAccount:
        await self.check_db()
        try:
            print("GetUserAccount", request)
            result = await queries.get_user_account(self.__db_conn__, request.user_id)
            if result is None:
                raise NotFoundError(request)
            return UserAccount(
                id=result["id"],
                user_name=result["UserName"],
                user_email=result["UserEmail"],
                user_phone=result["UserPhone"],
                user_address=result["UserAddress"],
                user_password="",
            )
        except Exception as e:
            print("Exception", e)
            raise InvalidArgument(argument="User not found", error=e)

    async def UpdateUserAccount(self, context, request: UserAccount) -> UserResponse:
        await self.check_db()
        try:
            result = await queries.update_user_account(self.__db_conn__, request)
            if result is None:
                raise NotFoundError(request)
            return UserResponse(
                message="updated user",
                user_id=result["id"],
                status="success",
            )
        except Exception as e:
            print("Exception", e)
            raise InvalidArgument(argument="User not found", error=e)

    # UserProfile
    async def CreateUserProfile(self, context, request: UserProfile) -> UserResponse:
        print("CreateUserProfile")
        print(request)
        return UserResponse(
            message="Hello, World!",
        )

    async def GetUserProfile(self, context, request: UserProfile) -> UserProfile:
        print("GetUserProfile")
        print(request)
        return UserProfile()

    async def ListUserProfile(
        self, context, request: GetUserRequest
    ) -> ListUserProfileResponse:
        print("ListUserProfile")
        print(request)
        return ListUserProfileResponse()

    async def UpdateUserProfile(self, context, request: UserProfile) -> UserResponse:
        return UserResponse()

    async def DeleteUserProfile(self, context, request: GetUserRequest) -> UserResponse:
        return UserResponse()

    # UserCVProfile
    async def ImportUserProfileFromCV(
        self, context, request: UserCVProfile
    ) -> UserResponse:
        raise InvalidArgument("Not implemented")

    async def CreateUserCVProfile(
        self, context, request: UserCVProfile
    ) -> UserResponse:
        raise InvalidArgument("Not implemented")
        return UserResponse()

    async def GetUserCVProfile(self, context, request: GetUserRequest) -> UserCVProfile:
        raise InvalidArgument("Not implemented")
        return UserCVProfile()
