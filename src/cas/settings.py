import os

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

ADMINS = [
    tuple(adm.split(':'))
    for adm in
    os.environ.get('ADMINS', '').split('\n')
    if adm
]

MANAGERS = [
    tuple(adm.split(':'))
    for adm in
    os.environ.get('MANAGERS', os.environ.get('ADMINS', '')).split('\n')
    if adm
]

DEBUG = False

if 'DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ.get('DB_USER', ''),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', ''),
            'PORT': os.environ.get('DB_PORT', ''),
        }
    }
else:
    DEBUG = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/app/src/cas/dev.sqlite',
        }
    }


DEBUG = os.environ.get('DEBUG', str(DEBUG)).lower() == 'True'


DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', '')
EMAIL_SUBJECT_PREFIX = os.environ.get('EMAIL_SUBJECT_PREFIX', '')
SECRET_KEY = os.environ.get('SECRET_KEY', '')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()
EMAILS_BASE_DOMAINS = os.environ.get('EMAILS_BASE_DOMAINS', '').split()
SECURE_PROXY_SSL_HEADER = os.environ.get('SECURE_PROXY_SSL_HEADER', '').split()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = os.environ.get('TIME_ZONE', 'Europe/Warsaw')

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'pl')

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

USE_TZ = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/app/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = '/app/static/'
STATIC_URL = '/static/'



SESSION_COOKIE_NAME = 'fnpcas'

GRAVATAR_DEFAULT_IMAGE = 'mm'
GRAVATAR_URL_PREFIX = 'https://www.gravatar.com/'

SITE_TITLE = 'Fundacja Wolne Lektury'


# Import localsettings file, which may override settings defined here
try:
    from .localsettings import *
except ImportError:
    pass



DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
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
    'ftp',
    'services.apps.ServicesConfig',
    'ssh_keys.apps.SshKeysConfig',

    'cas_provider',
    'django_gravatar',
    'oidc_provider',

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
LOGIN_URL = '/cas/login'
LOGOUT_URL = '/cas/logout'
LOGIN_REDIRECT_URL = '/accounts/'
CAS_CUSTOM_ATTRIBUTES_CALLBACK = 'cas.utils.custom_attributes_callback'


OIDC_USERINFO = 'emails.oidc.userinfo'

PASSWORD_HASHERS = (
    'cas.hashers.FNPBCryptPasswordHasher',
)

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ALLOWED_HOSTS = ALLOWED_HOSTS or ['*']
    SECRET_KEY = SECRET_KEY or 'dev-secret-key'
