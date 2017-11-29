"""
Django settings for smmpay project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+lk=nk)0ttp4_r7ekd=ojm3hm1lgfat1jza)b0*k$1ivgx)2x_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_db_logger',
    'ckeditor',
    'ckeditor_uploader',
    'smmpay.apps.account',
    'smmpay.apps.advert',
    'smmpay.apps.blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'smmpay.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'smmpay', 'templates')
        ],
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

WSGI_APPLICATION = 'smmpay.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': '',
        'HOST': '',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru'

LOCALE_PATHS = (os.path.join(BASE_DIR, 'smmpay', 'locale'),)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Sites

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'smmpay', 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'db_log': {
            'level': 'DEBUG',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler'
        },
    },
    'loggers': {
        'db': {
            'handlers': ['db_log'],
            'level': 'DEBUG'
        }
    }
}


# CKEditor

CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': '100%',
        'allowedContent': True,
        'removeFormatTags': '',
        'removeFormatAttributes': '',
        'protectedSource': ['/<i[^>]*><\/i>/g']
    },
}


# Account

LOGIN_URL = '/account/login'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 3

AUTH_USER_MODEL = 'account.User'

ACCOUNT_EMAIL_CHANGE_TIMEOUT_DAYS = 7


# Advert

ADVERT_MENU_POSITIONS = (
    ('top_menu', 'Top menu'),
    ('bottom_menu', 'Bottom menu')
)

ADVERT_CONTENT_BLOCK_POSITIONS = (
    ('sidebar', 'Sidebar'),
    ('header_menu', 'Header menu'),
    ('footer_menu', 'Footer menu'),
)


# Social networks settings

SOCIAL_NETWORK_VK_LOGIN = ''
SOCIAL_NETWORK_VK_PASSWORD = ''
SOCIAL_NETWORK_VK_APP_ID = ''

SOCIAL_NETWORK_FACEBOOK_KEY = ''
SOCIAL_NETWORK_FACEBOOK_SECRET = ''

SOCIAL_NETWORK_FACEBOOK_LOGIN = ''
SOCIAL_NETWORK_FACEBOOK_PASSWORD = ''

SOCIAL_NETWORK_TWITTER_API_KEY = ''
SOCIAL_NETWORK_TWITTER_API_SECRET = ''
SOCIAL_NETWORK_TWITTER_ACCESS_TOKEN = ''
SOCIAL_NETWORK_TWITTER_ACCESS_TOKEN_SECRET = ''

SOCIAL_NETWORK_YOUTUBE_API_KEY = ''