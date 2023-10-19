"""
Django settings for news_paper_project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dhjo!rz_+3*9v=yz+j)+fak*fpmg)%a6lup*9j92o&wz3bju@6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'django_filters',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    "django_apscheduler",
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
    
]

ROOT_URLCONF = 'news_paper_project.urls'
LOGIN_REDIRECT_URL = "/news"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'news_paper_project.wsgi.application'


ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / "static"]
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "soldat4ever@yandex.ru"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "soldat4ever@yandex.ru"


CELERY_BROKER_URL = f"redis://default:mqLiJmqiz59zG6oDYVAkMy7yXGKPFKX5@redis-14400.c265.us-east-1-2.ec2.cloud.redislabs.com:14400"
CELERY_RESULT_BACKEND = f"redis://default:mqLiJmqiz59zG6oDYVAkMy7yXGKPFKX5@redis-14400.c265.us-east-1-2.ec2.cloud.redislabs.com:14400"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'the_console_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default_formatter',
            'filters': ['require_debug_true']
        },
        'the_warning_handler': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'warning_formatter_style',
            'filters': ['require_debug_true']
        },
        'this_handler_works_if_error_critical': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'error_critical_formatter_style',
            'filters': ['require_debug_true']
        },
        'handler_for_general_log_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'not_default_formatter',
            'filters': ['require_debug_false']
        },
        'handler_for_errors_log_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'error_critical_formatter_style',
            'filters': ['require_debug_false']
        },
        'defender_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'not_default_formatter',
            'filters': ['require_debug_false']
        },
        'send_admin_mail_if_error': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'error_critical_formatter_style',
            'filters': ['require_debug_false']
        }
    },
    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'warning_formatter_style': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        'error_critical_formatter_style': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'not_default_formatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
    },
    'style': '{',
    'loggers': {
            'django': {
                'handlers': ['the_console_handler', 'the_warning_handler', 'this_handler_works_if_error_critical', 'handler_for_general_log_file',],
                'level': 'DEBUG',
                'propagate': True,
            },
            'django.request': {
                'handlers': ['handler_for_errors_log_file', 'send_admin_mail_if_error',],
                'level': 'ERROR',
                'propagate': True,
            },
            'django.server': {
                'handlers': ['handler_for_errors_log_file', 'send_admin_mail_if_error',],
                'propagate': True,
            },
            'django.template': {
                'handlers': ['handler_for_errors_log_file',],
                'level': 'ERROR',
                'propagate': True,
            },
            'django.db.backends': {
                'handlers': ['handler_for_errors_log_file',],
                'level': 'ERROR',
                'propagate': True,
            },
            'django.security': {
                'handlers': ['defender_log'],
                'level': 'INFO',
                'propagate': True,
            },

        },
}

#test just for fun
#ffffffff