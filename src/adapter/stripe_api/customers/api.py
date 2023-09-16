import stripe

from src.proj_fastapi_payments.config.setup import (
    STRIPE_API_KEY,
    STRIPE_API_BASE
)

from src.adapter.stripe_api.customers.dto import InvoiceSettings, Sources, Subscriptions, TaxIds, Customer

stripe.api_key = STRIPE_API_KEY
stripe.api_base = STRIPE_API_BASE


def find_customers():
    return stripe.Customer.list()


def retreive_customers(customer_id: str):
    # TODO: customer 없을때 예외처리 필요함
    customer = stripe.Customer.retrieve(customer_id)
    customer_invoice = InvoiceSettings(customer['invoice_settings'])
    customer_sources = Sources(**customer['sources'])
    customer_subscriptions = Subscriptions(**customer['subscriptions'])
    customer_tax_ids = TaxIds(**customer['tax_ids'])

    c = Customer(**customer)
    c.invoice_settings = customer_invoice
    c.sources = customer_sources
    c.subscriptions = customer_subscriptions
    c.tax_ids = customer_tax_ids

    return c


def create_customer(balance: int, email: str, description):
    return stripe.Customer.create(
        balance=balance,
        email=email,
        description=description
    )
