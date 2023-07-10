"""
Django settings for casa_de_cultura project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import platform
from django.contrib import messages
import os
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


sistema_operacional = platform.system()

if sistema_operacional != 'Windows':
    env = load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (os.getenv('DJANGO_DEBUG', 'True') == 'True')

if DEBUG or sistema_operacional == 'Windows':
    ALLOWED_HOSTS = ['*']
      
    SECRET_KEY = "django-insecure-w1+%=dnkf74)$0^ydxl*vm!xi^koj*0b#%@%bk*90@zz$&x&v@"
else:
    ALLOWED_HOSTS = ['.gusgewehr.com', '191.252.193.4', '127.0.0.1']
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "eventos.apps.EventosConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "casa_de_cultura.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "casa_de_cultura.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if DEBUG or sistema_operacional == 'Windows':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DJANGO_DB'],
            'USER': os.environ['DJANGO_DB_USER'],
            'PASSWORD': os.environ['DJANGO_DB_PASSWORD'],
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

if DEBUG and sistema_operacional == 'Windows':
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
else:
    STATIC_ROOT = '/var/cache/casa_de_cultura/static/'
    STATIC_URL = '/static/'

    MEDIA_ROOT = '/var/opt/casa_de_cultura/media/'
    MEDIA_URL = '/media/'

LOGOUT_REDIRECT_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



if not DEBUG and sistema_operacional != 'Windows':
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
            'format': '[%(asctime)s] %(levelname)s: '
                '%(message)s',
            }
        },
        'handlers': {
            'file': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': '/var/log/casa_de_cultura/casa_de_cultura.log',
                'when': 'midnight',
                'backupCount': 60,
                'formatter': 'default',
            },
        },
        'root': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    }