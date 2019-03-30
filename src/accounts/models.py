from cas_provider.signals import cas_collect_custom_attributes


def user_attributes(sender, user, **kwargs):
    return {
        'firstname': user.first_name,
        'lastname': user.last_name,
        'cn': ' '.join((user.first_name, user.last_name)),
        'email': user.email,
    }
cas_collect_custom_attributes.connect(user_attributes)
