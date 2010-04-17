def custom_attributes_callback(user):
    return {
        'email': user.email,
        'firstname': user.first_name,
        'lastname': user.last_name,
    }
