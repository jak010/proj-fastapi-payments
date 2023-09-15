from typing import Any

import stripe

from src.proj_fastapi_payments.config.setup import (
    STRIPE_API_KEY,
    STRIPE_API_BASE
)
import dataclasses
from stripe.stripe_object import StripeObject

stripe.api_key = STRIPE_API_KEY
stripe.api_base = STRIPE_API_BASE


@dataclasses.dataclass
class PlantDto:
    active: bool = None
    amount: str = None
    billing_scheme: str = None
    created: int = None
    currency: str = None
    id: str = None
    interval: str = None
    interval_count: str = None
    livemode: bool = None
    metadata: dict = None
    name: str = None
    nickname: str = None
    object: str = None
    product: str = None
    statement_descriptor: Any = None
    tiers: str = None
    tiers_mode: str = None
    trial_period_days: str = None
    usage_type: str = None

    def __post_init__(self):
        if isinstance(self.metadata, StripeObject):
            self.metadata = self.metadata.to_dict_recursive()

    def asdict(self):
        return dataclasses.asdict(self)


def retreieve_plan(id: str) -> PlantDto:
    return PlantDto(**stripe.Plan.retrieve(id=id))


def update_plan(
        active: bool = None,
        amount: str = None,
        billing_scheme: str = None,
        created: int = None,
        currency: str = None,
        id: str = None,
        interval: str = None,
        interval_count: str = None,
        livemode: bool = None,
        metadata: dict = None,
        name: str = None,
        nickname=None,
        object: str = None,
        product: str = None,
        statement_descriptor=None,
        tiers=None,
        tiers_mode=None,
        trial_period_days=None,
        usage_type: str = None
) -> PlantDto:
    return PlantDto(**stripe.Plan.modify(
        active=active,
        amount=amount,
        billing_scheme=billing_scheme,
        created=created,
        currency=currency,
        id=id,
        interval=interval,
        interval_count=interval_count,
        livemode=livemode,
        metadata=metadata,
        name=name,
        nickname=nickname,
        object=object,
        product=product,
        statement_descriptor=statement_descriptor,
        tiers=tiers,
        tiers_mode=tiers_mode,
        trial_period_days=trial_period_days,
        usage_type=usage_type
    ))
