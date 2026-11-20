from . import BASE_DOMAINS


def user_email(user):
    if BASE_DOMAINS:
        return f"{user.username}@{BASE_DOMAINS[0]}"
    return user.email


def userinfo(claims, user):
    """
    Claims for OIDC clients (see OIDC_USERINFO setting).

    `preferred_username` is used e.g. by Matrix-Synapse as the localpart
    and by Redmine (redmine_oauth) as the login.
    """
    email = user_email(user)
    claims.update({
        "preferred_username": user.username,
        "name": user.get_full_name() or user.username,
        "given_name": user.first_name,
        "family_name": user.last_name,
        "email": email,
        "email_verified": bool(email),
    })
    return claims
