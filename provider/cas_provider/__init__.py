from django.conf import settings

__all__ = []

_DEFAULTS = {
    'CAS_TICKET_EXPIRATION': 5, # In minutes
    'CAS_CUSTOM_ATTRIBUTES_CALLBACK': None,
}

for key, value in _DEFAULTS.iteritems():
    try:
        getattr(settings, key)
    except AttributeError:
        setattr(settings, key, value)
    except ImportError:
        pass