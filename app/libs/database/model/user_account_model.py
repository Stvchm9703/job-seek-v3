from peewee import *

from ._base import BaseModel
from libs.database import db_conn

"""
CREATE TABLE IF NOT EXISTS public.user_account
(
    id bigint NOT NULL DEFAULT nextval('user_account_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    user_name text COLLATE pg_catalog."default",
    user_password text COLLATE pg_catalog."default",
    user_email text COLLATE pg_catalog."default",
    user_phone text COLLATE pg_catalog."default",
    user_address text COLLATE pg_catalog."default",
    CONSTRAINT user_account_pkey PRIMARY KEY (id),
    CONSTRAINT fk_preference_keyword_user FOREIGN KEY (id)
        REFERENCES public.preference_keyword (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_survey_user_preference_user FOREIGN KEY (id)
        REFERENCES public.survey_user_preference (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_user_profile_user FOREIGN KEY (id)
        REFERENCES public.user_profile (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
"""


class UserAccountModel(BaseModel):
    class Meta:
        table_name = "user_account"
      
        schema = "public"
        database = db_conn
    user_name = TextField()
    user_password = TextField()
    user_email = TextField()
    user_phone = TextField()
    user_address = TextField()
    pass
