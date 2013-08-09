from django.conf import settings as _settings

view_settings = dict((k, getattr(_settings, k)) for k in
    _settings.TEMPLATE_CONTEXT_SETTINGS)

def settings(request):
    return {'settings': view_settings}
