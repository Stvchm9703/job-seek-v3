from libs.twirp_protos import user_management_twirp

# from libs.protos.job_seek.user_management import UserResponse
# from libs.protos.job_seek.prediction import SurveyUserPerfenceRequest
from libs.database import init_db
import uvicorn
import sys

from twirp.asgi import TwirpASGIApp
from twirp.exceptions import InvalidArgument

from .service import UserManagementService


def main():
    service = user_management_twirp.UserManagementServiceServer(
        service=UserManagementService(),
    )

    app = TwirpASGIApp()
    app.add_service(service)

    config = uvicorn.Config(
        app,
        port=5200,
        reload=True,
        log_level="debug",
        access_log=True,
        reload_dirs=["app/services/service_user_management", "app/libs"],
    )
    server = uvicorn.Server(config)

    server.run()
