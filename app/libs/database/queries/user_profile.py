import datetime
from typing import Union
import surrealdb
import sys

import libs.protos.job_seek.user_management as um_pb

from libs.database.model import UserProfileModel


async def create_user_profile(connection, dataset) -> str:
    user = UserProfileModel.create_from_proto(dataset)
    user.save()
    return f"{user.id}"


async def get_user_profile(connection, profile_id: str):
    user = UserProfileModel.get_by_id(profile_id)
    if user:
        return user.to_proto()
    return None


async def list_user_profile(connection, user_id):
    profiles = UserProfileModel.select().where(UserProfileModel.user.id == user_id)
    if profiles:
        return [profile.to_proto() for profile in profiles]
    return None


async def update_user_profile(connection, dataset):
    user = UserProfileModel.get_by_id(dataset.id)
    if user:
        user.update_from_proto(dataset)
        user.save()
        return user.to_proto()

    return None


async def delete_user_profile(connection, profile_id):
    user = UserProfileModel.get_by_id(profile_id)
    if user:
        user.delete()
        return True
    return None
