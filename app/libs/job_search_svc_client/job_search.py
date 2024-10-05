import threading
import traceback
from typing import Optional
from libs.twirp_protos import user_management_twirp

# import prediction_twirp
from twirp.exceptions import InvalidArgument
import libs.database.queries.user_account as ua_queries
import libs.database.queries.user_profile as up_queries
import libs.database.queries.survey_user_preference as sup_queries

import libs.protos.job_seek.user_management as um_pb
import libs.protos.job_seek.prediction as pr_pb
import libs.protos.job_seek.job_search as js_pb

# from libs.database import init_db

from grpclib.client import Channel


CHANNEL_HOST = "localhost"
CHANNEL_PORT = 60010


# async def job_search_request(conn, request: Optional[pr_pb.SurveyUserPerfenceRequest]):

#     channel = Channel(CHANNEL_HOST, CHANNEL_PORT)
#     service = js_pb.JobSearchServiceStub(channel)
#     response = await service.job_search(params)
#     channel.close()

#     return response


async def user_profile_prefetch_job_search(
    params: Optional[pr_pb.SurveyUserPerfenceRequest],
):
    channel = Channel(CHANNEL_HOST, CHANNEL_PORT)
    service = js_pb.JobSearchServiceStub(channel)
    response = await service.user_job_search(params)
    channel.close()

    return response
