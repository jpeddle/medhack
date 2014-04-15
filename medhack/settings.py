"""
Django settings for medhack project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

from django.conf import global_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import pytz

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# <BASE_DIR>/data/
DATA_DIR = os.path.join(BASE_DIR, 'data')
# <BASE_DIR>/data/csv/
CSV_DIR = os.path.join(DATA_DIR, 'csv')


# The env variable should have a value of 'dev', 'test', 'prod'
ENV_VARIABLE = 'MEDHACK_ENV'
MODE = os.getenv(ENV_VARIABLE) or 'dev'

DEFAULT_DB_NAME = 'medhack'

DB_USER = 'medhack'
DB_PASSWORD = 'M3DH@CK'

if MODE == "dev":
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    HTTP_PORT = 8000

    MYSQL_HOST = 'localhost'

    DATABASE = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

elif MODE == "test":
    # SECURITY WARNING: don't run with debug turned on in production!
    # TODO this should be: DEBUG = False
    DEBUG = True

    HTTP_PORT = 8007

    MYSQL_HOST = 'localhost'
    DB_NAME = "%s_%s" % (DEFAULT_DB_NAME, 'test')

    DATABASE = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': DB_NAME,
            'USER': DB_USER, # Not used with sqlite3.
            'PASSWORD': DB_PASSWORD, # Not used with sqlite3.
            'HOST': MYSQL_HOST, # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '', # Set to empty string for default. Not used with sqlite3.
        }
    }

elif MODE == "prod":
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    MYSQL_HOST = None

    HTTP_PORT = None

    ES_HOST = None
    ES_PORT = None
    ES_INDEX_NAME = None

    USE_COMPILED_STYLES = None
    USE_COMPILED_JS = None
    GA_TRACKING = None

    DATABASE = None

else:
    DEBUG = None

    MYSQL_HOST = None

    HTTP_PORT = None

    ES_HOST = None
    ES_PORT = None
    ES_INDEX_NAME = None

    USE_COMPILED_STYLES = None
    USE_COMPILED_JS = None
    GA_TRACKING = None

    DATABASE = None

    print "Environment variable '$%s' is currently [%s]" % (ENV_VARIABLE, MODE)
    print "Please set the environment variable $%s to one of the following: 'dev', 'test' or 'prod'" % ENV_VARIABLE
    exit(1)



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(m-ahv0-1np_o+@_sq3zgtl7dvvgdqs^$4swkhiylc34ffa=^7'


TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost'
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # More Django apps
    'crispy_forms',

    # Other apps
    # devserver is currently broken for django 1.6+
    # 'devserver',
    'django_extensions',

    # Our apps
    'src.apps.office_admin',
    'src.apps.office',
    'src.apps.patient',
    'src.apps.schedule',
    'src.apps.visit',
    'src.ui',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    os.path.join(os.path.join(os.path.join(BASE_DIR, 'src'), 'ui', 'templates')),
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'medhack.urls'

WSGI_APPLICATION = 'medhack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'
PYTZ_TIMEZONE = pytz.timezone(TIME_ZONE)

SEND_TWILIO = True

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.join(os.path.join(BASE_DIR, 'src'), 'ui', 'static')),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#crispy_form settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = not DEBUG

MEDHACK_LOG = 'medhack'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ' %(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['special']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        MEDHACK_LOG: {
            'handlers': ['console'], #, 'mail_admins'],
            'level': 'DEBUG',
            # 'filters': ['special']
        },
    }
}
