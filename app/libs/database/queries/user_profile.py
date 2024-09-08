import datetime
from typing import Union
import surrealdb
import sys

import libs.protos.job_seek.user_management as um_pb


async def create_user_profile(connection: surrealdb.Surreal, dataset) -> str:
    print("create_user_profile in db")
    keyword_list = []
    for kwt_set in dataset.keywords:
        if kwt_set.kw_id == "" or kwt_set is None or kwt_set.kw_id == "-":
            result_kw = await connection.create(
                f"PreferenceKeyword",
                {
                    "UserId": kwt_set.user_id,
                    "Keyword": kwt_set.keyword,
                    "Value": kwt_set.value,
                    "Type": kwt_set.type,
                    "IsPositive": kwt_set.is_positive,
                },
            )
        else:
            result_kw = await connection.update(
                dataset.kw_id,
                {
                    "UserId": kwt_set.user_id,
                    "Keyword": kwt_set.keyword,
                    "Value": kwt_set.value,
                    "Type": kwt_set.type,
                    "IsPositive": kwt_set.is_positive,
                },
            )
        keyword_list.append(result_kw[0]["id"])

    result = await connection.create(
        "UserProfile",
        {
            "Company": dataset.company,
            "Description": dataset.description,
            "EndDate": dataset.end_date,
            "Keywords": keyword_list,
            "Position": dataset.position,
            "Salary": dataset.salary,
            "StartDate": dataset.start_date,
            "Title": dataset.title,
            "Type": str(um_pb.UserProfileType(dataset.type)),
            "UserId": dataset.user_id,
        },
    )
    return result[0]


async def get_user_profile(connection: surrealdb.Surreal, profile_id: str):

    query_profile_id = (
        profile_id if "UserProfile:" in profile_id else f"UserProfile:{profile_id}"
    )

    result = connection.query(
        f"""SELECT *, (SELECT * FROM PreferenceKeyword WHERE id in $parent.Keywords) AS Keywords as keywords FROM {query_profile_id}"""
    )

    return result[0]


async def list_user_profile(connection: surrealdb.Surreal, user_id):
    result = await connection.query(
        f"""
SELECT *,
(SELECT * FROM PreferenceKeyword  WHERE id in $parent.Keywords ) AS Keywords
FROM UserProfile
WHERE UserId = $user_id
        """,
        {"user_id": user_id},
    )
    return result[0]["result"]


async def update_user_profile(connection: surrealdb.Surreal, dataset):
    profile_id = dataset.id if dataset.id else None
    if not profile_id:
        raise ValueError("userId is required to update user profile")

    if "UserProfile:" not in profile_id:
        profile_id = f"UserProfile:{profile_id}"

    # keywords update
    keyword_list = []
    for kwt_set in dataset.keywords:
        if kwt_set.kw_id == "" or kwt_set is None or kwt_set.kw_id == "-":
            keyword_id = await connection.create(
                f"PreferenceKeyword",
                {
                    "UserId": kwt_set.user_id,
                    "Keyword": kwt_set.keyword,
                    "Value": kwt_set.value,
                    "Type": kwt_set.type,
                    "IsPositive": kwt_set.is_positive,
                },
            )
        else:
            keyword_id = await connection.update(
                dataset.kw_id,
                {
                    "UserId": kwt_set.user_id,
                    "Keyword": kwt_set.keyword,
                    "Value": kwt_set.value,
                    "Type": kwt_set.type,
                    "IsPositive": kwt_set.is_positive,
                },
            )

        keyword_list.append(keyword_id[0]["id"])
        print(keyword_id)

    result = await connection.update(
        profile_id,
        {
            "Company": dataset.company,
            "CompanyDetail": None,
            "Description": dataset.description,
            "EndDate": dataset.end_date,
            # "Keywords": "DEFINE FIELD Keywords ON UserProfile TYPE option<array<record<PreferenceKeyword>>> PERMISSIONS FULL",
            # "Keywords[*]": "DEFINE FIELD Keywords[*] ON UserProfile TYPE record<PreferenceKeyword> PERMISSIONS FULL",
            "Keywords": keyword_list,
            "Position": dataset.position,
            "Salary": dataset.salary,
            "StartDate": dataset.start_date,
            "Title": dataset.title,
            "Type": dataset.type,
            "UserId": dataset.user_id,
        },
    )
    return result[0]


async def delete_user_profile(connection: surrealdb.Surreal, profile_id: str) -> str:
    if "UserProfile:" in profile_id:
        result = await connection.delete(profile_id)
    elif profile_id != "":
        result = await connection.delete(f"UserProfile:{profile_id}")

    return result
