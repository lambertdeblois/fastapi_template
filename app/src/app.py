import os
from fastapi import FastAPI

from .routers import hello


def create_app(env=None):

    app = FastAPI()

    app.include_router(hello.hello)

    return app