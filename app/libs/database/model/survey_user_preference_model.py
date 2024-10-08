from peewee import *
# from libs.database.model import BaseModel, db_conn
from ._base import BaseModel
from .preference_keyword_model import PreferenceKeywordModel
from .user_account_model import UserAccountModel
from libs.database import db_conn

"""

CREATE TABLE IF NOT EXISTS public.survey_user_preference
(
    id bigint NOT NULL DEFAULT nextval('survey_user_preference_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    user_id bigint,
    survey_id bigint,
    CONSTRAINT survey_user_preference_pkey PRIMARY KEY (id),
    CONSTRAINT fk_survey_user_preference_user FOREIGN KEY (user_id)
        REFERENCES public.user_account (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

"""


class SurveyUserPreferenceModel(BaseModel):
    class Meta:
        table_name = "survey_user_preference"
        schema = "public"
        database = db_conn

    # user_id = BigIntegerField()
    user = ForeignKeyField(UserAccountModel, backref="survey_user_preferences")
    survey_id = BigIntegerField()
    keywords = ForeignKeyField(
        PreferenceKeywordModel,
        backref="survey_user_preference",
        constraint_name="fk_survey_user_preference_keywords",
        null=True,
    )
    pass
