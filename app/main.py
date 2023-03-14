from fastapi import FastAPI
from app.api.routes import users


def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(users.router)
    return application


app = get_application()
