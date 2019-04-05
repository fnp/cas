from os import path

PROJECT_ROOT = path.realpath(path.dirname(__file__))

DEBUG = True

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
TIME_ZONE = 'UTC'

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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            PROJECT_ROOT + '/templates',
        ],
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
            'debug': DEBUG,
        },
    },
]

LOCALE_PATHS = (
    PROJECT_ROOT + '/locale',
)

INSTALLED_APPS = (
    'accounts.apps.AccountsConfig',
    'emails.apps.EmailsConfig',
    'services.apps.ServicesConfig',
    'ssh_keys.apps.SshKeysConfig',

    'cas_provider',
    'django_gravatar',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# django-cas-provider settings
LOGIN_URL = '/cas/login/'
LOGOUT_URL = '/cas/logout/'
LOGIN_REDIRECT_URL = '/accounts/'
CAS_CUSTOM_ATTRIBUTES_CALLBACK = 'cas.utils.custom_attributes_callback'
SESSION_COOKIE_NAME = 'fnpcas'

GRAVATAR_DEFAULT_IMAGE = 'mm'
GRAVATAR_URL_PREFIX = 'https://www.gravatar.com/'

SITE_TITLE = 'Fundacja Nowoczesna Polska'

# Import localsettings file, which may override settings defined here
try:
    from .localsettings import *
except ImportError:
    pass
