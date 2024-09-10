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


async def frist_patch_job_search_request(
    conn, request: Optional[pr_pb.SurveyUserPerfenceRequest]
):
    print("job_search")
    profiles = await up_queries.list_user_profile(conn, request.user_id)
    profile_set = extract_profile_keyword(profiles)

    survey_set = extract_survey_keyword(request, profile_set)

    params = js_pb.JobSearchRequest(
        user_id=request.user_id,
        salary_type=0,
        min_salary=request.min_salary,
        max_salary=request.max_salary,
        work_type=survey_set["work_type"],
        classification=request.classification,
        company_size=survey_set["company_size"],
        work_locale=request.work_locale,
        # post_id=request.post_id,
        # company_id=request.company_id,
        keywords=survey_set["keywords"],
        # total_count=request.total_count,
        # page_number=1,
        page_size=20,
        # cache_ref=request.cache_ref,
        # allow_mix_cache=request.allow_mix_cache,
    )

    channel = Channel("localhost", 62001)
    service = js_pb.JobSearchServiceStub(channel)
    response = await service.job_search(params)
    channel.close()

    return response


def extract_survey_keyword(
    request: Optional[pr_pb.SurveyUserPerfenceRequest], profile_set: dict
):
    keywords = profile_set["keywords"]
    work_type = 0
    company_size = 2
    location = []
    classification = []
    min_salary = profile_set['last_job']['salary']
    max_salary = profile_set['last_job']['salary']
    for keyword in request.keywords:
        if keyword.keyword == "role_type":
            if keyword.value == "full_time":
                work_type = 0
            elif keyword.value == "part_time":
                work_type = 1
            elif keyword.value == "contract":
                work_type = 3

        elif keyword.keyword == "company_scale":
            if keyword.value == "international":
                company_size = 5
            elif keyword.value == "local":
                company_size = 2
            else:
                company_size = None

        elif keyword.keyword == "work_model":
            if keyword.value == "remote":
                location.append("remote")

        elif keyword.keyword == "job_industry":
            if keyword.value == "last_industry":
                classification.append("last_industry")

        elif keyword.keyword == "job_title":
            if keyword.value == "same_title":
                # classification.append("last_title")
                keywords.append(keyword.value)

        else:
            keywords.append(keyword.value)

    return {
        "keywords": keywords,
        "work_type": work_type,
        "company_size": company_size,
        "location": location,
        "classification": classification,
        "min_salary": request.min_salary,
        "max_salary": request.max_salary,
    }


def extract_profile_keyword(profiles):
    keywords = []
    title = []

    for profile in profiles:
        title.append(profile["title"])

        # keywords.append(profile['Keywords']["Value"])

        if profiles["Type"] == "STUDENT":
            keywords.append(profile["Title"])

    return {
        "title": title,
        "keywords": keywords,
        # last_job
        "last_job": profiles.sort(key=lambda x: x.end_date, reverse=True)[0],
    }
