"""
Django settings for askmath project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os, config

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as message_constants

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.join(os.path.split(__file__)[0], '..'))

path = lambda *args: os.path.join(PROJECT_PATH, *args)

SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', ]

# Authentication

AUTH_PROFILE_MODULE = 'authentication.User'
AUTH_USER_MODEL = 'authentication.User'


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
)

THIRD_PARTY_APPS = (
    'rosetta',
    'django_js_reverse',
)

LOCAL_APPS = (
    'base',
    'ask',
    'authentication',
    'forum',
    'partners_admin',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #add to translate
    'django.middleware.locale.LocaleMiddleware',
    #add to timezone
    'base.middleware.timezone.TimezoneMiddleware',
]

ROOT_URLCONF = 'askmath.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'base/templates',
            'ask/templates',
            'authentication/templates',
            'forum/templates',
            'partners_admin/templates',
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

WSGI_APPLICATION = 'askmath.wsgi.application'

#Authentication
LOGIN_URL = reverse_lazy("authentication:account_login")
LOGIN_REDIRECT_URL = reverse_lazy("ask:home")
LOGOUT_URL = reverse_lazy("authentication:account_logout")



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.DATABASE_ENGINE,
        'NAME': config.DATABASE_NAME,
        'USER': config.DATABASE_USER,
        'PASSWORD': config.DATABASE_PASSWORD,
        'HOST': config.DATABASE_HOST,
        'PORT': config.DATABASE_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/


FORMAT_MODULE_PATH = [
    'askmath.formats',
]

from askmath.formats.pt_BR.formats import * #GAMBI

LOCALE_PATHS = (
    path('askmath/locale'),
    path('base/locale'),
    path('ask/locale'),
    path('authentication/locale'),
    path('forum/locale'),
    path('partners_admin/locale'),
    '/var/local/translations/locale',
)

LANGUAGES = (
    ('pt-br', _('Brazilian Portuguese')),
    ('en', _('English')),
    ('es', _('Spanish')),
)

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = path('static/')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path('base/static/'),
    path('ask/static/'),
    path('authentication/static/'),
    path('forum/static/'),
    path('/usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/admin/'),
)

MEDIA_ROOT = path('media/')
MEDIA_URL = '/media/'

# Media uploads dirs

ISSUE_PHOTO_DIR = 'uploads/issue_photo/%Y/%m/%d'
SOCIAL_NETWORK_ICON_DIR = 'uploads/social_network_icon/%Y/%m/%d'
USER_AVATAR_DIR = 'uploads/user_avatar'

# Pagination

PAGINATE_BY = 10

# MessagesTAGS

MESSAGE_TAGS = {
    message_constants.DEBUG: 'debug',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

# Session

SESSION_COOKIE_NAME = "askmath_sessionid"
CSRF_COOKIE_NAME = "askmath_csrftoken"
LANGUAGE_COOKIE_NAME = "askmath_language"

#Email

EMAIL_ADMINS = config.EMAIL_ADMINS
DEFAULT_FROM_EMAIL = config.DEFAULT_FROM_EMAIL

EMAIL_HOST = config.EMAIL_HOST
EMAIL_HOST_USER = config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config.EMAIL_HOST_PASSWORD
EMAIL_PORT = config.EMAIL_PORT
EMAIL_USE_TLS = config.EMAIL_USE_TLS
EMAIL_BACKEND = config.EMAIL_BACKEND

