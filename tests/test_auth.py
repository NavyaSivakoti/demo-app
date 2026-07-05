from app.auth import login


def test_login_valid_user():
    # Fails: valid credentials are wrongly rejected (intentional bug in login()).
    assert login("alice", "correct-horse-battery") is True


def test_login_rejects_bad_password():
    assert login("alice", "nope") is False
