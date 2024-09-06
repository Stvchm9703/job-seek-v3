import surrealdb

DB_HOST = "192.168.0.102"
DB_PORT = 8654
DB_NS = "job-seek"
DB_DATABASE = "development"
# DB_USER = "job_seek_prediction_service"
# DB_PASS = "jobseek_prediction"

DB_USER = "root"
DB_PASS = "root"


async def init_db():
    connection_url = f"ws://{DB_HOST}:{DB_PORT}/rpc"
    db_conn = surrealdb.Surreal(connection_url)
    await db_conn.connect()
    await db_conn.signin({"user": DB_USER, "pass": DB_PASS})
    await db_conn.use(DB_NS, DB_DATABASE)
    return db_conn
