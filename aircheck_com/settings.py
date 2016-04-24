"""
Django settings for aircheck_com project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zl!lwx+hkd8oky9qk%lhe7)eir3o%2^_9x4%4wy2+s9-w#s)#_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DEBUG', True))
template_debug = bool(os.environ.get('TEMPLATE_DEBUG', DEBUG))
TESTING = bool(os.environ.get('TESTING', False))

# Custom Global App Config
PROJECT_NAME = 'aircheck'
PROJECT_DOMAIN = 'airchecknasa.com'

APP_ENV = os.environ.get('APP_ENV', '').upper()

STAGING = PRODUCTION = False

if APP_ENV == 'STAGING':
    STAGING = True
elif APP_ENV == 'PRODUCTION':
    PRODUCTION = True
    DEBUG = template_debug = False
else:
    DEBUG = template_debug = True

# Allowed Hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', PROJECT_DOMAIN, '.' + PROJECT_DOMAIN, 'dev.' + PROJECT_DOMAIN, 'staging.' + PROJECT_DOMAIN]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'aircheck_com.urls'

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

WSGI_APPLICATION = 'aircheck_com.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if not PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'aircheck-mysql',
            'USER': 'bfee9ded82f84f',
            'PASSWORD': '2c211575',
            'HOST': 'us-cdbr-azure-west-c.cloudapp.net',
            'PORT': '3306',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

#
# Custom Settings
#

# My Apps

INSTALLED_APPS += (
    'django.contrib.sitemaps',
    # custom apps
    'accounts',
    'nasa',
    'pages',
    'sensors',
    'sentiments',
)

ADMINS = (
    ('Chris Del Guercio', 'cdelguercio@gmail.com'),
)

VERSION = '0_2'

API_VERSION = 'v1'

if STAGING or PRODUCTION:
    STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
else:
    STATIC_ROOT = os.path.join(PROJECT_ROOT, "static_collected")

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {}
}

LOGGING['loggers'][PROJECT_NAME] = {
    'handlers': ['mail_admins'],
    'level': 'ERROR',
    'propagate': True,
}

# Test logging

LOGGING['loggers'][PROJECT_NAME + '-test'] = {
    'handlers': ['console'],
    'level': 'INFO',
    'propagate': True,
}

# DisallowedHost

LOGGING['loggers']['django.security.DisallowedHost'] = {
    'handlers': ['null'],
    'propagate': False,
}

# Django Request Error Logging

LOGGING['loggers']['django.request'] = {
    'handlers': ['mail_admins'],
    'level': 'ERROR',
    'propagate': True,
}

# Django Extensions

INSTALLED_APPS += [
    'django_extensions',
]

# Impersonate

MIDDLEWARE_CLASSES += [
    'slothauth.middleware.ImpersonateMiddleware',
]

# Authentication

ACCOUNT_NATURAL_KEY = 'email'
AUTHENTICATION_BACKENDS = [
    'slothauth.backends.PasswordlessAuthentication',
]

# Django Rest Framework

INSTALLED_APPS += [
    'rest_framework',
    'rest_framework.authtoken'
]

'''
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 9999,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
}
'''

# SlothAuth

INSTALLED_APPS += [
    'slothauth',
]

ACCOUNT_EMAIL_DOMAIN = PROJECT_DOMAIN

ACCOUNT_EMAIL_PASSWORD_RESET_SUBJECT = 'AirCheck Password Reset'

ACCOUNT_EMAIL_FROM = 'help@' + PROJECT_DOMAIN

ACCOUNT_EMAIL_PASSWORDLESS_LOGIN_SUBJECT = 'AirCheck Login Link'

AUTH_USER_MODEL = 'accounts.Account'

# Template

SETTINGS_PASSED_TO_TEMPLATE = ['VERSION']
