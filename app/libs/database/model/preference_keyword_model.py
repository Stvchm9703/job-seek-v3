from peewee import *
from ._base import BaseModel
from libs.database import db_conn

"""
CREATE TABLE IF NOT EXISTS public.preference_keyword
(
    id bigint NOT NULL DEFAULT nextval('preference_keyword_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    keyword text COLLATE pg_catalog."default",
    value text COLLATE pg_catalog."default",
    type text COLLATE pg_catalog."default",
    is_positive boolean,
    CONSTRAINT preference_keyword_pkey PRIMARY KEY (id),
    CONSTRAINT fk_survey_user_preference_keywords FOREIGN KEY (id)
        REFERENCES public.survey_user_preference (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_user_profile_keywords FOREIGN KEY (id)
        REFERENCES public.user_profile (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
"""

class PreferenceKeywordModel(BaseModel):
    class Meta:
        table_name = "preference_keyword"
        schema = "public"
        database = db_conn

    user_id = BigAutoField()
    keyword = TextField()
    value = TextField()
    type = TextField()
    is_positive = BooleanField()
    pass
