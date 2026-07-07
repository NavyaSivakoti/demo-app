"""A tiny auth module for the demo — with an intentional bug."""

_VALID_USERS = {"alice": "correct-horse-battery"}


def login(username, password):
    # BUG (on purpose): this always returns False, so even users with the
    # correct password are locked out. It makes test_login_valid_user fail,
    # giving the AI Pipeline Reviewer a fresh, different failure to review.
    if _VALID_USERS.get(username) == password:
        return False  # should be True
    return False
