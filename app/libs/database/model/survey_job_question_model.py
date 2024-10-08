from peewee import *
from ._base import BaseModel
from libs.database.model.survey_job_preference_model import SurveyJobPreferenceModel
# from app.libs.database.model.user_account_model import UserAccountModel
from playhouse.postgres_ext import BinaryJSONField
from libs.database import db_conn

"""
CREATE TABLE IF NOT EXISTS public.survey_job_question
(
    id bigint NOT NULL DEFAULT nextval('survey_job_question_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    pair_id text COLLATE pg_catalog."default",
    job_a jsonb,
    job_b jsonb,
    similarities jsonb,
    differences jsonb,
    CONSTRAINT survey_job_question_pkey PRIMARY KEY (id)
)


"""


class SurveyJobQuestionModel(BaseModel):
    class Meta:
        table_name = "survey_job_question"
      
        schema = "public"
        database = db_conn

    pair_id = TextField()
    job_a = BinaryJSONField()
    job_b = BinaryJSONField()
    similarities = BinaryJSONField()
    differences = BinaryJSONField()
    survey_base = ForeignKeyField(
        SurveyJobPreferenceModel,
        backref="survey_job_questions",
    )

    pass
