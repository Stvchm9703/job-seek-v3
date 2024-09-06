import grpc
import grpc._utilities
import grpclib

from .survey_user_perfence import store_survey_user_perfence

from libs.twirp_protos import prediction_twirp
from libs.twirp_protos.prediction_twirp import PredictionServiceServer
from libs.protos.job_seek.user_management import UserResponse
from libs.protos.job_seek.prediction import SurveyUserPerfenceRequest
from libs.database import init_db
import uvicorn
import sys

# prediction_twirp._sym_db.RegisterMessage(UserResponse)
# prediction_twirp._sym_db.RegisterMessage(SurveyUserPerfenceRequest)

sys.path.append("app/libs/twirp_protos")
from prediction_pb2 import *
from user_management_pb2 import *


# import prediction_twirp
import twirp
from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument


class PredictionService(object):

    async def SurveyUserPerfence(
        self, context, request: SurveyUserPerfenceRequest
    ) -> UserResponse:
        print("survey_user_perfence")
        print(request)

        try:
            await store_survey_user_perfence(request)
        except Exception as e:
            print(e)

        return UserResponse(
            message="Hello, World!",
        )

    async def GetSurveyJob(self, context, request):
        pass

    async def SurveyJobPerfence(self, context, request):
        pass

    async def PredictJobMatchScore(self, context, request):
        pass

    async def ExtractJobKeywords(self, context, request):
        pass

    async def ExtractUserProfileKeywords(self, context, request):
        pass

    async def GenerateCoverLetter(self, context, request):
        pass

    async def GenerateCV(self, context, request):
        pass


def main():
    service = PredictionServiceServer(
        service=PredictionService(),
    )

    app = TwirpASGIApp()
    app.add_service(service)

    config = uvicorn.Config(
        app,
        port=5000,
        reload=True,
    )
    server = uvicorn.Server(config)

    server.run()
