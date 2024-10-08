from peewee import *
from ._base import BaseModel
from libs.database import db_conn
"""
CREATE TABLE IF NOT EXISTS public.company_detail
(
    id bigint NOT NULL DEFAULT nextval('company_detail_id_seq'::regclass),
    created_at timestamp with time zone,
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    reference_id text COLLATE pg_catalog."default",
    name text COLLATE pg_catalog."default",
    url text COLLATE pg_catalog."default",
    linkedin text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    industry text COLLATE pg_catalog."default",
    job_posted bigint,
    group_size text COLLATE pg_catalog."default",
    head_quarters text COLLATE pg_catalog."default",
    specialties text COLLATE pg_catalog."default",
    locations text COLLATE pg_catalog."default",
    CONSTRAINT company_detail_pkey PRIMARY KEY (id)
)
"""


class CompanyDetailModel(BaseModel):

    reference_id = TextField()
    name = TextField(null=True)
    url = TextField(null=True)
    linkedin = TextField(null=True)
    description = TextField(null=True)
    industry = TextField(null=True)
    job_posted = BigIntegerField(null=True)
    group_size = TextField(null=True)
    head_quarters = TextField(null=True)
    specialties = TextField(null=True)
    locations = TextField(null=True)

    class Meta:
        schema = "public"
        database = db_conn
        table_name = "company_detail"

    pass
