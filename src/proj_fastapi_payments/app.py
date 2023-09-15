from fastapi import FastAPI
from src.proj_fastapi_payments.config import setup


class Application:

    def __init__(self, app):
        self.app = app

    def __call__(self, *args, **kwargs):
        setup.routers(app=self.app)

        return self.app


application = Application(app=FastAPI())
