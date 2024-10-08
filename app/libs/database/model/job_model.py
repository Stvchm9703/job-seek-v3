from peewee import *

from libs.database.model.company_detail_model import CompanyDetailModel
from ._base import BaseModel
from libs.database import db_conn

"""
CREATE TABLE IF NOT EXISTS public.job
(
    id bigint NOT NULL DEFAULT nextval('job_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    post_id text COLLATE pg_catalog."default",
    post_title text COLLATE pg_catalog."default",
    post_url text COLLATE pg_catalog."default",
    pay_range text COLLATE pg_catalog."default",
    debug_text text COLLATE pg_catalog."default",
    hitted_keywords text COLLATE pg_catalog."default",
    score bigint,
    role text COLLATE pg_catalog."default",
    work_type text COLLATE pg_catalog."default",
    locations text COLLATE pg_catalog."default",
    expiring_date text COLLATE pg_catalog."default",
    CONSTRAINT job_pkey PRIMARY KEY (id)
)
"""

class JobModel(BaseModel):
    class Meta:
        table_name = "job"
        schema = "public"
        database = db_conn
    post_id = TextField()
    post_title = TextField()
    post_url = TextField()
    pay_range = TextField(null=True)
    debug_text = TextField(null=True)
    hitted_keywords = TextField(null=True)
    score = BigIntegerField(null=True)
    role = TextField(null=True)
    work_type = TextField(null=True)
    locations = TextField(null=True)
    expiring_date = TextField(null=True)
    company_detail = ForeignKeyField(
        CompanyDetailModel,
        backref="jobs",
        constraint_name="fk_job_company_detail",
    )
    pass
