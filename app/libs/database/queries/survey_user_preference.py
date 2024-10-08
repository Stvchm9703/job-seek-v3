from datetime import datetime, timezone
import surrealdb
import sys

from libs.database.model import (
    PreferenceKeywordModel,
    UserProfileModel,
    SurveyUserPreferenceModel,
)


async def create_survey_user_preference(connection, dataset):
    user_profile_result = UserProfileModel.get_by_id(dataset.user_id)

    # user_profile_redsult = await connection.select(f"UserProfile:{dataset.user_id}")
    # user_profile = user_profile_redsult[0]

    if user_profile_result is None:
        raise Exception("Cannot find user profile")

    # print(user_profile)

    keyword_list = []

    for kwt_set in dataset.keywords:
        keyword_set = PreferenceKeywordModel.create(**kwt_set)
        keyword_list.append(keyword_set)

    # survey_user_preference_id = await connection.create(
    #     "SurveyUserPreference",
    #     {
    #         "UserId": user_profile.user_id,
    #         "Keywords": keyword_list,
    #         "CreatedAt": datetime.now(timezone.utc).astimezone().isoformat(),
    #     },
    # )

    # print(survey_user_preference_id)

    result = (
        SurveyUserPreferenceModel.create(
            user_id=user_profile_result.id,
            keywords=keyword_list,
        )
        .returning(SurveyUserPreferenceModel.id)
        .namedtuples()
        .execute()
    )

    return result[0].id
