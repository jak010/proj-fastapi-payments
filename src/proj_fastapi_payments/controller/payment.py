from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse

from src.adapter import stripe_api

payment_router = APIRouter(tags=['Payment'], prefix="/v1/payment")


@payment_router.get(path="/plans")
def get_subscription_plans():
    plans = stripe_api.plans.api.find_plans()
    return JSONResponse(content={"data": [plan.asdict() for plan in plans]})


@payment_router.get(path="/plans/{plan_id}")
def get_subscription_plan(plan_id: str = Path()):
    plan = stripe_api.plans.api.retreieve_plan(plan_id)
    return JSONResponse(content={"data": plan.asdict()})


@payment_router.get(path="/customers/{customer_id}")
def get_customers(
        customer_id: str = Path()
):
    customer = stripe_api.customers.api.retreive_customers(customer_id=customer_id)
    return customer
