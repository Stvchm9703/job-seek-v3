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
import asyncio


def process_job_search_request(connection, request):
    print("process_job_search_request")
    print(request)

    thread1 = threading.Thread(target=job_search_request, args=(connection, request))
    thread1.start()
    thread1.join()
    print("thread1.join()")

