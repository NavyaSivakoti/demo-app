from app.payments import create_charge


def test_charge_default_usd():
    assert create_charge(100)["currency"] == "USD"


def test_charge_eur():
    # Fails because create_charge ignores the currency argument (intentional bug).
    charge = create_charge(100, "EUR")
    assert charge["currency"] == "EUR"
