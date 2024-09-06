import sys
from typing import List

sys.path.append("app/libs/twirp_protos")
from libs.protos.job_seek.user_management import UserProfile
from prediction_pb2 import *
from user_management_pb2 import *


from libs.protos.job_seek.prediction import SurveyUserPerfenceRequest
from libs.protos.job_seek.job_search import JobSearchRequest


from libs.database import init_db
from libs.database.queries.survey_user_preference import create_survey_user_preference, list_user_profile

db_conn = None


async def check_db_conn():
    global db_conn
    if db_conn is None:
        db_conn = await init_db()
    return True

async def store_survey_user_perfence(request: SurveyUserPerfenceRequest):
    global db_conn
    # print("store_survey_user_perfence")
    # print(request)
    await check_db_conn()

    if request.user_id == "":
        raise Exception("User ID is required")

    # survey_id
    await create_survey_user_preference(db_conn, request)

    return True


def create_job_search_params(request: SurveyUserPerfenceRequest, user_profile: List[UserProfile] ) -> JobSearchRequest:
    
    
    return JobSearchRequest(
        user_id=request.user_id,
        salary_type=0,
        keywords=request.keywords
    )


async def fetch_survey_job():

    return [] 
