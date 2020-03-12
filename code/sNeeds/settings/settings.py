"""
Django settings for sNeeds project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "..", "templates")

INSTALLED_APPS = [
    'rest_framework',
    'django_filters',  # for filtering get queries in DRF
    'drf_yasg',  # for filtering get queries in DRF
    'corsheaders',
    'django_rest_passwordreset',
    'polymorphic',  # For django-polymorphic

    'sNeeds.apps.customAuth',
    'sNeeds.apps.account',
    'sNeeds.apps.consultants',
    'sNeeds.apps.store',
    'sNeeds.apps.docs',
    'sNeeds.apps.carts',
    'sNeeds.apps.orders',
    'sNeeds.apps.comments',
    'sNeeds.apps.payments',
    'sNeeds.apps.userfiles',
    'sNeeds.apps.discounts',
    'sNeeds.apps.videochats',
    'sNeeds.apps.chats',
    'sNeeds.apps.storePackages',
    'sNeeds.apps.webinars',

    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_cleanup',  # should go after your apps
]
# Imported key to prevent circular imports.
from .secure import keys

SECRET_KEY = os.environ.get('SECRET_KEY')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS, should be at first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # For per-request translation
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sNeeds.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sNeeds.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = True
TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "..", "files"),
]

MEDIA_URL = '/files/'
MEDIA_ROOT = 'files'

AUTH_USER_MODEL = 'customAuth.CustomUser'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST_IP'),
        'PORT': os.environ.get('DB_HOST_PORT'),
    }
}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, '..', 'translations'),
]

from .config.JWTAuthConfig import JWT_AUTH

# Loading API keys
from .celery.celery_config import *

# APIs
from .secure import APIs

SKYROOM_API_KEY = APIs.skyroom
SENDINBLUE_API_KEY = APIs.sendinblue
ZARINPAL_MERCHANT = APIs.zarinpal_merchant

# Keys
ALL_SKYROOM_USERS_PASSWORD = keys.ALL_SKYROOM_USERS_PASSWORD
