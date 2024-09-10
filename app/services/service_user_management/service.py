import traceback
from libs.twirp_protos import user_management_twirp

from libs.database import init_db

import sys

sys.path.append("app/libs/twirp_protos")
from user_management_pb2 import (
    UserAccount,
    UserProfile,
    UserCVProfile,
    GetUserRequest,
    ListUserProfileResponse,
    UserResponse,
    PreferenceKeyword,
)


# import prediction_twirp
from twirp.exceptions import InvalidArgument, TwirpServerException
import twirp.errors as errors
import libs.database.queries.user_account as ua_queries
import libs.database.queries.user_profile as up_queries

from services import NotFoundError 

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
            result = await ua_queries.create_user_account(self.__db_conn__, request)
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
            result = await ua_queries.get_user_account(
                self.__db_conn__, request.user_id
            )
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
            result = await ua_queries.update_user_account(self.__db_conn__, request)
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

        await self.check_db()
        try:
            result = await up_queries.create_user_profile(self.__db_conn__, request)
            return UserResponse(
                message=f"success create user profile, id:{result['id']}, user_id:{result['UserId']}",
                user_id=result["id"],
                status="success",
            )
        except Exception as e:
            # print("exception ", e)
            # print(e.__cause__)
            traceback.print_exc()
            raise InvalidArgument(argument="Create user profile failed", error=e)

    async def GetUserProfile(self, context, request: UserProfile) -> UserProfile:
        await self.check_db()
        try:
            print("GetUserAccount", request)
            result = await up_queries.get_user_profile(self.__db_conn__, request.id)
            if result is None:
                raise NotFoundError(request)

            keywords = []
            for kw in result['Keywords']:
                keywords.append(
                    PreferenceKeyword(
                        kw_id=kw['id'],
                        user_id=kw['UserId'],
                        keyword=kw['Keyword'],
                        value=kw['Value'],
                        type=kw['Type'],
                        is_positive=kw['IsPositive'],
                    )
                )

            return UserProfile(
                id=result['id'],
                user_id=result['UserId'],
                title=result['Title'],
                description=result['Description'],
                position=result['Position'],
                company=result['Company'],
                start_date=result['StartDate'],
                end_date=result['EndDate'],
                salary=result['Salary'],
                keywords=keywords,
            )
        except Exception as e:
            print("Exception", e)
            raise InvalidArgument(argument="UserProfile not found", error=e)

    async def ListUserProfile(
        self, context, request: GetUserRequest
    ) -> ListUserProfileResponse:

        await self.check_db()
        try:
            result = await up_queries.list_user_profile(
                self.__db_conn__, request.user_id
            )
            print("ListUserProfile", result)
            if result is None:
                raise NotFoundError(request)

            msg_pack = ListUserProfileResponse(
                user_id=request.user_id, status="success", message="listed", profiles=[]
            )

            # profiles = []
            for prf in result:
                keyword = []
                for kw in prf['Keywords']:
                    keyword.append(
                        PreferenceKeyword(
                            kw_id=kw['id'],
                            user_id=kw['UserId'],
                            keyword=kw['Keyword'],
                            value=kw['Value'],
                            type=kw['Type'],
                            is_positive=kw['IsPositive'],
                        )
                    )
                msg_pack.profiles.append(
                    UserProfile(
                        id=prf['id'],
                        user_id=prf['UserId'],
                        title=prf['Title'],
                        position=prf['Position'],
                        description=prf['Description'],
                        company=prf['Company'],
                        start_date=prf['StartDate'],
                        end_date=prf['EndDate'],
                        salary=prf['Salary'],
                        company_detail=None,
                        keywords=keyword,
                    )
                )

            return msg_pack

        except Exception as e:
            print("Exception", e)
            raise InvalidArgument(argument="UserProfile not found", error=e)

    async def UpdateUserProfile(self, context, request: UserProfile) -> UserResponse:

        await self.check_db()
        try:
            result = await up_queries.update_user_profile(self.__db_conn__, request)
            return UserResponse(
                message=f"success create user profile, id:{result['id']}, user_id:{result['UserId']}",
                user_id=result['id'],
                status="success",
            )
        except Exception as e:
            print("exception ", e)
            raise InvalidArgument(argument="Create user profile failed", error=e)

    async def DeleteUserProfile(self, context, request: GetUserRequest) -> UserResponse:
        print(request)

        await self.check_db()
        try:
            result = await up_queries.delete_user_profile(self.__db_conn__, request.id)
            return UserResponse(
                message=f"success create user profile, id:{request.id}, user_id:{request.user_id}",
                user_id=result.id,
                status="success",
            )
        except Exception as e:
            print("exception ", e)
            raise InvalidArgument(argument="Create user profile failed", error=e)

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
