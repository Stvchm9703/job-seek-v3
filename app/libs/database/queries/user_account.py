# import datetime
from typing import Union

# import surrealdb
# import sys
import pprint
from libs.database.model.user_account_model import UserAccountModel
import libs.protos.job_seek.user_management as um_pb


async def create_user_account(connection, dataset) -> str:
    # print("create_user_account in db")
    # pprint.pprint(dataset)
    # result = await connection.create(
    #     "UserAccount",
    #     {
    #         "UserName": dataset.user_name,
    #         "UserEmail": dataset.user_email,
    #         "UserPhone": dataset.user_phone,
    #         "UserPassword": dataset.user_password,
    #         "UserAddress": dataset.user_address,
    #     },
    # )
    # print(result)
    result = UserAccountModel.create_from_proto(dataset)
    return result


async def get_user_account(connection, user_id: str) -> um_pb.UserAccount:
    # print("get_user_account in db", user_id)
    # if "UserAccount:" in user_id:
        # result = await connection.select(user_id)
    # elif user_id != "":
        # result = await connection.select(f"UserAccount:{user_id}")

    if user_id == "":
        raise ValueError("userId is required to get user account")
    result = UserAccountModel.get_by_id(user_id)
    
    return result


async def search_user_account(
    connection, dataset: dict
) -> um_pb.ListUserProfileResponse:
    print("search_user_account in db")

    result = UserAccountModel.select().where(
        UserAccountModel.user_name == dataset["user_name"]
        or UserAccountModel.user_email == dataset["user_email"]
        or UserAccountModel.user_phone == dataset["user_phone"]
    )
    print(result)
    
    return result


async def update_user_account(connection, dataset) -> str:
    print("update_user_account in db")
    user_id = dataset.id if dataset.id else None
    if not user_id:
        raise ValueError("userId is required to update user account")

    print("user_id", user_id)
    # result = await connection.update(
    #     user_id,
    #     {
    #         "UserName": dataset.user_name,
    #         "UserEmail": dataset.user_email,
    #         "UserPhone": dataset.user_phone,
    #         "UserPassword": dataset.user_password,
    #         "UserAddress": dataset.user_address,
    #     },
    # )
    # print(result)

    result = UserAccountModel.update_from_proto(dataset)
    
    
    return result
