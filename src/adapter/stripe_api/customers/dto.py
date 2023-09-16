from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class InvoiceSettings:
    default_payment_method: str


@dataclass
class Sources:
    data: list
    has_more: bool
    object: str
    total_count: int
    url: str


@dataclass
class Subscriptions:
    data: list
    has_more: bool
    object: str
    total_count: int
    url: str


@dataclass
class TaxIds:
    data: list
    has_more: bool
    object: str
    total_count: int
    url: str


@dataclass
class Customer:
    account_balance: int
    address: str
    business_vat_id: str
    created: int
    currency: str
    default_source: str
    delinquent: bool
    description: str
    discount: str
    email: str
    id: str
    livemode: bool
    metadata: dict
    name: str
    object: str
    phone: str
    preferred_locales: str
    shipping: str

    invoice_settings: Optional[InvoiceSettings] = None
    sources: Optional[Sources] = None
    subscriptions: Optional[Subscriptions] = None
    tax_ids: Optional[TaxIds] = None
