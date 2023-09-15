import stripe

from src.proj_fastapi_payments.config.setup import (
    STRIPE_API_KEY,
    STRIPE_API_BASE
)

stripe.api_key = STRIPE_API_KEY
stripe.api_base = STRIPE_API_BASE


def create_customer(balance: int, email: str, description):
    return stripe.Customer.create(
        balance=balance,
        email=email,
        description=description
    )


# customer = create_customer(balance=9999, email="test@test.com", description="test")
""" Customer Data
{
  "account_balance": -9999,
  "address": null,
  "business_vat_id": null,
  "created": 1694803249,
  "currency": "eur",
  "default_source": null,
  "delinquent": false,
  "description": "test",
  "discount": null,
  "email": "test@test.com",
  "id": "cus_SyWEJxksFHMSMA",
  "invoice_settings": {
    "default_payment_method": null
  },
  "livemode": false,
  "metadata": {},
  "name": null,
  "object": "customer",
  "phone": null,
  "preferred_locales": null,
  "shipping": null,
  "sources": {
    "data": [],
    "has_more": false,
    "object": "list",
    "total_count": 0,
    "url": "/v1/customers/cus_SyWEJxksFHMSMA/sources"
  },
  "subscriptions": {
    "data": [],
    "has_more": false,
    "object": "list",
    "total_count": 0,
    "url": "/v1/customers/cus_SyWEJxksFHMSMA/subscriptions"
  },
  "tax_ids": {
    "data": [],
    "has_more": false,
    "object": "list",
    "total_count": 0,
    "url": "/v1/customers/cus_SyWEJxksFHMSMA/tax_ids"
  }
} 
"""
