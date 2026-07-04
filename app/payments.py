"""A tiny payments module for the demo — with an intentional bug."""


def create_charge(amount, currency="USD"):
    # BUG (on purpose): ignores `currency` and always charges in USD.
    # This makes test_charge_eur fail, so the CI pipeline goes red and the
    # AI Pipeline Reviewer has something real to review.
    return {"amount": amount, "currency": "USD"}
