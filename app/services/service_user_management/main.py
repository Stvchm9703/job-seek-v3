import grpc
import grpc._utilities
import grpclib

from .survey_user_perfence import store_survey_user_perfence

from libs.twirp_protos import user_management_twirp
# from libs.protos.job_seek.user_management import UserResponse
# from libs.protos.job_seek.prediction import SurveyUserPerfenceRequest
from libs.database import init_db
import uvicorn
import sys

# prediction_twirp._sym_db.RegisterMessage(UserResponse)
# prediction_twirp._sym_db.RegisterMessage(SurveyUserPerfenceRequest)

sys.path.append("app/libs/twirp_protos")
from user_management_pb2 import *


# import prediction_twirp
import twirp
from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument


class UserManagementService(object):

    async def CreateUserAccount(self, context, request: UserAccount) -> UserResponse:
        print("CreateUserAccount")
        print(request)

        return UserResponse(
            message="Hello, World!",
        )

    async def GetUserProfile(self, context, request: GetUserRequest) -> UserAccount:
        print("GetUserProfile")
        print(request)

        return UserProfile()

    async def UpdateUserProfile(self, context, request: UpdateUserProfileRequest) -> UserResponse:

        print("UpdateUserProfile")
        print(request)

        return UserResponse(
            message="Hello, World!",
        )

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
      
      
    async def ListUserProfile(self, context, request: GetUserRequest) -> ListUserProfileResponse:
        print("ListUserProfile")
        print(request)
        return ListUserProfileResponse()
      
    async def UpdateUserProfile(self, context, request: UserProfile) -> UserResponse:
        return UserResponse()
      
    async def DeleteUserProfile(self, context, request: GetUserRequest) -> UserResponse:
        return UserResponse()
      
    async def ImportUserProfileFromCV(self, context, request: UserCVProfile) -> UserResponse:
        return UserResponse()
      
    async def CreateUserCVProfile(self, context, request: UserCVProfile) -> UserResponse:
        return UserResponse()
      
    async def GetUserCVProfile(self, context, request: GetUserRequest) -> UserCVProfile:
        return UserCVProfile()

def main():
    service = user_management_twirp.UserManagementServiceServer(
        service=UserManagementService(),
    )

    app = TwirpASGIApp()
    app.add_service(service)

    config = uvicorn.Config(
        app,
        port=5200,
        reload=True,
    )
    server = uvicorn.Server(config)

    server.run()
