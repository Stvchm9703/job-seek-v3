# import surrealdb
import os
import pprint
from dotenv import load_dotenv, find_dotenv, get_key
import subprocess
# from peewee import *
from playhouse.postgres_ext import PostgresqlExtDatabase

load_dotenv()

print(find_dotenv())
_ENV_FILE = find_dotenv()
DB_HOST = get_key(dotenv_path=_ENV_FILE, key_to_get="DB_HOST") or "127.0.0.1"
DB_PORT = get_key(dotenv_path=_ENV_FILE, key_to_get="DB_PORT") or 5432
DB_NS = get_key(dotenv_path=_ENV_FILE, key_to_get="DB_NS") or "job_seeker"
DB_DATABASE = get_key(dotenv_path=_ENV_FILE, key_to_get="DB_DATABASE") or "development"
# DB_USER = "job_seek_prediction_service"
# DB_PASS = "jobseek_prediction"
DB_USER = (
    get_key(dotenv_path=_ENV_FILE, key_to_get="DB_USER") or "user_management_service"
)
DB_PASS = (
    get_key(dotenv_path=_ENV_FILE, key_to_get="DB_PASS") or "service_user_management"
)

db_conn = None


def init_db():
    db_conn = PostgresqlExtDatabase(
        DB_NS, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
    )
    db_conn.connect()
    return db_conn


def migrate_db():
    print("migrate_db")
    # python -m pwiz -e postgresql my_postgres_db > mymodels.py
    pprint.pprint(
        {
            "DB_HOST": DB_HOST,
            "DB_PORT": DB_PORT,
            "DB_NS": DB_NS,
            "DB_DATABASE": DB_DATABASE,
            "DB_USER": DB_USER,
            "DB_PASS": DB_PASS,
        }
    )
    table_list = [
        "company_detail",
        "job",
        "user_account",
        "user_profile",
        "survey_user_preference",
        "survey_job_preference",
    ]
    for table in table_list:
        # fmt: off
        proc = subprocess.Popen(
             " ".join([
                "python", "-m", "pwiz",
                "-e", "postgresql",
                "-u", DB_USER,
                "-P", DB_PASS,
                "-H", DB_HOST,
                "-s", "public"
                "-p", DB_PORT,
                "-t", table, 
                DB_NS, ">",
                f"app/libs/database/model/{table}_model.py"
            ]),
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        # fmt: on
        output, errr = proc.communicate(DB_PASS.encode())
    pass
