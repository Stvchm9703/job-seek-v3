import datetime
from typing import Union
import surrealdb
import sys

import libs.protos.job_seek.user_management as um_pb


async def create_user_account(connection: surrealdb.Surreal, dataset) -> str:
    result = await connection.create(
        "UserAccount",
        {
            "UserName": dataset.user_name,
            "UserEmail": dataset.user_email,
            "UserPhone": dataset.user_phone,
            "UserPassword": dataset.user_password,
            "UserAddress": dataset.user_address,
        },
    )
    return result[0]


async def get_user_account(
    connection: surrealdb.Surreal, user_id: str
) -> um_pb.UserAccount:
    print("get_user_account in db", user_id)
    if "UserAccount:" in user_id:
        result = await connection.select(user_id)
    elif user_id != "":
        result = await connection.select(f"UserAccount:{user_id}")

    print(result)

    return result


async def search_user_account(
    connection: surrealdb.Surreal, dataset: dict
) -> um_pb.ListUserProfileResponse:
    print("search_user_account in db")
    result = await connection.query(
        f"SELECT * FROM UserAccount WHERE user_name = $user_name OR user_email = $user_email OR user_phone = $user_phone",
        dataset,
    )
    return result


async def update_user_account(
    connection: surrealdb.Surreal, dataset
) -> str:
    print("update_user_account in db")
    user_id = dataset.id if dataset.id else None
    if not user_id:
        raise ValueError("userId is required to update user account")

    if "UserAccount:" not in user_id:
        user_id = f"UserAccount:{user_id}"

    print("user_id", user_id)
    result = await connection.update(
        user_id,
        {
            "UserName": dataset.user_name,
            "UserEmail": dataset.user_email,
            "UserPhone": dataset.user_phone,
            "UserPassword": dataset.user_password,
            "UserAddress": dataset.user_address,
        },
    )
    print(result)
    return result
