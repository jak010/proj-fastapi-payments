from fastapi import APIRouter
from fastapi import Path
from fastapi.responses import JSONResponse

from src.adapter import stripe_api

payment_router = APIRouter(tags=['Payment'], prefix="/v1/payment")


@payment_router.get(path="/plan/{plan_id}")
def get_subscription_plan(plan_id: str = Path()):
    plan = stripe_api.plan.retreieve_plan(id=plan_id)
    return JSONResponse(content={"data": plan.asdict()})

