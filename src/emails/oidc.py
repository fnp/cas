from . import BASE_DOMAINS


def userinfo(claims, user):
    return {
        "email": f"{user.username}@{BASE_DOMAINS[0]}"
    }
