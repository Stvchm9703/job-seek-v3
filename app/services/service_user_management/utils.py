import asyncio
from pprint import pprint
import re
import threading
from libs.protos.job_seek.job_search import JobSearchRequest

from libs.job_search_svc_client import job_search as js_svc


def create_user_profile_job_params(profile):
    pprint(profile)

    if profile is None:
        return None

    salary_set = list(map(lambda x: int(x) * 1000, profile.salary.split(" - ")))
    location = (profile.location + "").replace("undefined", "").replace(",", "")
    # check if location is start with a number
    if re.match(r"^\d+\,", location):
        location = re.sub(r"^\d+\,", "", location)

    keywords = []
    for kw_set in profile.keywords:
        keywords.append(kw_set.value)
        # if kw_set.keyword == "industry":
        #     industry = kw_set.value

    if profile.type == 1:  # Employee

        classification = 0
        if (
            profile.position is not None
            and "{" in profile.position
            and "}" in profile.position
        ):
            result = re.findall(r"\d+", profile.position)
            classification = int(result[0]) if result and result[0] else 0

        keywords.append("!" + profile.title)

        return JobSearchRequest(
            user_id=profile.user_id,
            salary_type=0,
            min_salary=int(salary_set[0] * 0.8) if salary_set[0] is not None else None,
            max_salary=int(salary_set[1] * 1.5) if salary_set[1] is not None else None,
            work_type=None,
            classification=classification,
            company_size=None,
            work_locale=location,
            keywords=keywords,
            page_size=20,
        )

    if ";" in profile.title:
        titles = profile.title.split(";")
        keywords.append(titles[-1])

    # elif profile.type == 0: # Student
    return JobSearchRequest(
        user_id=profile.user_id,
        salary_type=0,
        min_salary=None,
        max_salary=None,
        work_type=None,
        classification=None,
        company_size=None,
        work_locale=location,
        keywords=keywords,
        page_size=20,
    )


async def thread_process_job_search_request(request):
    job_search_params = create_user_profile_job_params(request)
    print("job_search_params", job_search_params)

    # thread1 = threading.Thread(
    #     target=async_wrapper_user_profile_prefetch_job_search,
    #     args=[job_search_params],
    # )
    # thread1.start()
    await js_svc.user_profile_prefetch_job_search(job_search_params)


def async_wrapper_user_profile_prefetch_job_search(request):
    asyncio.run(js_svc.user_profile_prefetch_job_search(request))
