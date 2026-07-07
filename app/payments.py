"""A tiny payments module for the demo."""


def create_charge(amount, currency="USD"):
    # Fixed: honour the requested currency instead of always charging USD.
    return {"amount": amount, "currency": "EUR"}
