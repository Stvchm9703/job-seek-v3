import datetime
import surrealdb
import sys

sys.path.append("app/libs/twirp_protos")
from prediction_pb2 import *
from user_management_pb2 import *


async def create_survey_user_preference(
    connection: surrealdb.Surreal, dataset: SurveyUserPerfenceRequest
):
    user_profile = await connection.select(f"UserProfile:{dataset.user_id}")

    if user_profile is None:
        raise Exception("Cannot find user profile")

    keyword_list = []

    for kwt_set in dataset.keywords:
        keyword_id = await connection.create(
            f"PreferenceKeyword",
            {
                "UserId": user_profile.user_id,
                "Keyword": kwt_set.keyword,
                "Value": kwt_set.value,
                "Type": kwt_set.type,
                "IsPositive": kwt_set.is_positive,
            },
        )

        print(keyword_id)
        keyword_list.append(keyword_id)

    survey_user_preference_id = await connection.create(
        "SurveyUserPreference",
        {
            "UserId": user_profile.user_id,
            "Keywords": list(map(lambda x: f"PreferenceKeyword:{x['id']}", keyword_list)),
            "CreatedAt": datetime.now(),
        },
    )

    print(survey_user_preference_id)

    return True


async def list_user_profile(connection,  user_id: str):
    if user_id == "":
        raise Exception("User ID is required")

    result = await connection.query(
        f"""
SELECT *,
(SELECT * FROM PreferenceKeyword  WHERE id in $parent.Keywords ) AS Keywords
FROM UserProfile:{user_id}
"""
    )

    if result is None:
        raise Exception("Cannot find user profile")

    return result['Results']
