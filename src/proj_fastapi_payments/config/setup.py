from fastapi import FastAPI

STRIPE_API_KEY = "sk_test_12345:"
STRIPE_API_BASE = "http://localhost:8420"


def routers(app: FastAPI):
    from src.proj_fastapi_payments.controller.payment import payment_router

    for router in [payment_router]:
        app.include_router(router)
