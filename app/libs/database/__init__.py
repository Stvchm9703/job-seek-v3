import surrealdb
import os
import pprint
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.environ.get("DB_HOST") or "127.0.0.1"
DB_PORT = os.environ.get("DB_PORT") or 8654
DB_NS = os.environ.get("DB_NS") or "job-seek"
DB_DATABASE = os.environ.get("DB_DATABASE") or "development"
# DB_USER = "job_seek_prediction_service"
# DB_PASS = "jobseek_prediction"

DB_USER = os.environ.get("DB_USER") or "root"
DB_PASS = os.environ.get("DB_PASS") or "root"


async def init_db():
    connection_url = f"ws://{DB_HOST}:{DB_PORT}/rpc"
    db_conn = surrealdb.Surreal(connection_url)
    await db_conn.connect()
    await db_conn.signin({"user": DB_USER, "pass": DB_PASS})
    await db_conn.use(DB_NS, DB_DATABASE)
    return db_conn
