from peewee import *
from ._base import BaseModel
from .preference_keyword_model import PreferenceKeywordModel
from .user_account_model import UserAccountModel
from libs.database import db_conn

"""
CREATE TABLE IF NOT EXISTS public.user_profile
(
    id bigint NOT NULL DEFAULT nextval('user_profile_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    title text COLLATE pg_catalog."default",
    "position" text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    company text COLLATE pg_catalog."default",
    salary text COLLATE pg_catalog."default",
    type text COLLATE pg_catalog."default",
    start_date text COLLATE pg_catalog."default",
    end_date text COLLATE pg_catalog."default",
    CONSTRAINT user_profile_pkey PRIMARY KEY (id)
)
"""


class UserProfileModel(BaseModel):
    class Meta:
        table_name = "user_profile"
        schema = "public"
        database = db_conn

    user = ForeignKeyField(UserAccountModel, backref="user_profiles")
    title = TextField()
    position = TextField()
    description = TextField()
    company = TextField()
    salary = TextField()
    type = TextField()
    start_date = TextField()
    end_date = TextField()
    keywords = ForeignKeyField(
        PreferenceKeywordModel,
        backref="user_profile",
        constraint_name="fk_user_profile_keywords",
        null=True,
    )
    pass
