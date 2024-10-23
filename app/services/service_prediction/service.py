from pprint import pprint
import traceback

# import prediction_twirp
from twirp.exceptions import InvalidArgument
import services.service_prediction.subprocess as sp
import libs.database_v1.queries.user_account as ua_queries
import libs.database_v1.queries.user_profile as up_queries
import libs.database_v1.queries.survey_user_preference as sup_queries
from libs.database_v1 import init_db
import json

import sys

sys.path.append("app/libs/twirp_protos")
from prediction_pb2 import (
    SurveyUserPerfenceRequest,
    GetSurveyJobRequest,
    GetSurveyJobResponse,
)
from user_management_pb2 import (
    UserResponse,
    UserProfile,
)

from services import NotFoundError, UnimplementedError


class PredictionService(object):
    __db_conn__ = None

    async def check_db_conn(self):
        if self.__db_conn__ is None:
            self.__db_conn__ = init_db()
        return True

    async def SurveyUserPerfence(
        self, context, request: SurveyUserPerfenceRequest
    ) -> UserResponse:
        print("survey_user_perfence")
        print(request)

        await self.check_db_conn()

        try:
            result = await sup_queries.create_survey_user_preference(
                self.__db_conn__, request
            )

            # jobList = await sp.frist_patch_job_search_request(self.__db_conn__, request)

            return UserResponse(
                message="created survey user preference",
                user_id=result["id"],
                status="success",
            )

        except Exception as e:
            print("exception", e)
            traceback.print_exc()
            raise InvalidArgument(
                argument="Create survey user preference failed", error=e
            )

    async def GetSurveyJob(
        self, context, request: GetSurveyJobRequest
    ) -> GetSurveyJobResponse:

        await self.check_db_conn()

        try:
            # result = await sup_queries.get_survey_job(self.__db_conn__, request)
            sample_data = json.load(
                open("app/services/service_prediction/sample_result.json")
            )
            pprint(sample_data)
            for job in sample_data["jobs"]:
                job["job_id"] = str(job["job_id"])

            return GetSurveyJobResponse(
                user_id=request.user_id,
                survey_id=request.survey_id,
                jobs=[],
            )

        except Exception as e:
            print("exception", e)
            traceback.print_exc()
            raise NotFoundError(request)

    async def SurveyJobPerfence(self, context, request):
        return UnimplementedError("SurveyJobPerfence")
        pass

    async def PredictJobMatchScore(self, context, request):
        return UnimplementedError("PredictJobMatchScore")

        pass

    async def ExtractJobKeywords(self, context, request):
        return UnimplementedError("ExtractJobKeywords")
        pass

    async def ExtractUserProfileKeywords(self, context, request):
        return UnimplementedError("ExtractUserProfileKeywords")
        pass

    async def GenerateCoverLetter(self, context, request):
        return UnimplementedError("GenerateCoverLetter")
        pass

    async def GenerateCV(self, context, request):
        return UnimplementedError("GenerateCV")
        pass
