"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2p^$=h+sniwttdhoy(t0-$_sl5alcgf88^kiss$vc_8t^wihl2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'django.contrib.gis',

    #3rd Party Modules
    'rest_framework',
    'rest_framework.authtoken',
    'rest_registration',
    'django_extensions',
    'storages',
    'django_filters',
    'cities_light',
    'cities',

    #My Modules
    'attendance',
    'blog',
    'calendars',
    'commons',
    'commons2',
    'companies',
    'customers',
    'datacom',
    'employees',
    'inventory',
    'invoices',
    'leads',
    'partners',
    'salesoffices',
    'users',
    'vendors',
    'vthpp',
    'warehouses',
    'financial',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    #     'rest_framework.renderers.BrowsableAPIRenderer',
    # ),
    'DEFAULT_PERMISSIONS_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated'
        'rest_framework.permissions.AllowAny',
    )
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_URL': 'https://frontend-url/reset-password/',
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
    'VERIFICATION_FROM_EMAIL': 'no-reply@example.com',
}

try:
    from .local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write(
        "Warning: Can't find the file 'local_settings.py' in the directory containing {}. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n"
        .format(__file__))
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()
		
AUTH_USER_MODEL = 'users.User'

# Media Files including Bafcodes
MEDIA_ROOT = os.path.join(BASE_DIR, '/media/')
STATIC_ROOT = '/static/'
MEDIA_URL = '/media/'

AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

CITIES_LIGHT_INCLUDE_COUNTRIES = ['US']

EVENTTOOLS_REPEAT_CHOICES = (
    ("RRULE:FREQ=DAILY", 'Daily'),
    ("RRULE:FREQ=WEEKLY", 'Weekly'),
    ("RRULE:FREQ=MONTHLY", 'Monthly'),
    ("RRULE:FREQ=YEARLY", 'Yearly'),
)

#GeoSpatial Database Settings
GEOS_LIBRARY_PATH = '/usr/local/lib/libgeos_c.so'
GDAL_LIBRARY_PATH = '/usr/local/lib/libgdal.so'
CITIES_CONTINENT_DATA = {
    'NA': ('North America', 6255149),
}
CITIES_LOCALES = ['en']
CITIES_POSTAL_CODES = ['US']