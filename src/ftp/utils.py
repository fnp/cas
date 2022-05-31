import secrets


def generate_password(length=10):
    return secrets.token_urlsafe(length)
