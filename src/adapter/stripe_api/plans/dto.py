import dataclasses

from stripe.stripe_object import StripeObject
from typing import Any


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
