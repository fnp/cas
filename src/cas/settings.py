# -*- coding: utf-8 -*-
from os import path

PROJECT_ROOT = path.realpath(path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = [
]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': path.join(PROJECT_ROOT, 'dev.sqlite'), # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = path.join(PROJECT_ROOT, '../../media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = path.join(PROJECT_ROOT, '../../static/')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    path.join(PROJECT_ROOT, 'static'),
]

ROOT_URLCONF = 'cas.urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT + '/templates',
)

LOCALE_PATHS = (
    PROJECT_ROOT + '/locale-contrib',
    PROJECT_ROOT + '/locale',
)

INSTALLED_APPS = (
    'accounts',

    'cas_provider',
    'fnpdjango',
    'honeypot',
    'south',
    'django_libravatar',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook', 
    'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.persona',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',

)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'honeypot.middleware.HoneypotMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    "cas.context_processors.settings",
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# django-cas-provider settings
LOGIN_URL = '/cas/login/'
LOGOUT_URL = '/cas/logout/'
LOGIN_REDIRECT_URL = '/accounts/'
CAS_CUSTOM_ATTRIBUTES_CALLBACK = 'cas.utils.custom_attributes_callback'
SESSION_COOKIE_NAME = 'fnpcas'

REGISTRATION_OPEN = True
TEMPLATE_CONTEXT_SETTINGS = ('REGISTRATION_OPEN',)

ACCOUNT_EMAIL_VERIFICATION = None
SOCIALACCOUNT_AUTO_SIGNUP = False
SOCIALACCOUNT_AVATAR_SUPPORT = False
SOCIALACCOUNT_ADAPTER = 'cas.social.LooseSocialAccountAdapter'

SOCIALACCOUNT_PROVIDERS = {
    'openid': {
        'SERVERS': [
            dict(id='google',
                  name='Google',
                  openid_url='https://www.google.com/accounts/o8/id')
        ]
    }
}


CONTRIB_LOCALE_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.openid',
]

# Import localsettings file, which may override settings defined here
try:
    from localsettings import *
except ImportError:
    pass
