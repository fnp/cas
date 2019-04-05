from django.conf import settings


BASE_DOMAINS = getattr(settings, 'EMAILS_BASE_DOMAINS', [])
