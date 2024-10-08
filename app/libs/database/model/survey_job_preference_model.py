from peewee import *

from libs.database.model.user_account_model import UserAccountModel
from ._base import BaseModel
from libs.database import db_conn

"""
CREATE TABLE IF NOT EXISTS public.survey_job_preference
(
    id bigint NOT NULL DEFAULT nextval('survey_job_preference_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    user_id bigint,
    survey_id bigint,
    CONSTRAINT survey_job_preference_pkey PRIMARY KEY (id),
    CONSTRAINT fk_survey_job_preference_user FOREIGN KEY (user_id)
        REFERENCES public.user_account (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

"""


class SurveyJobPreferenceModel(BaseModel):
    class Meta:
        table_name = "survey_job_preference"
      
        schema = "public"
        database = db_conn

    user = ForeignKeyField(UserAccountModel, backref="survey_job_preferences", constraint_name="fk_survey_job_preference_user")
    survey_id = BigIntegerField()

    # question = ForeignKeyField(
    pass
