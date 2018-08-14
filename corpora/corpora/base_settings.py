# -*- coding: utf-8 -*-
"""
Django settings for corpora project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import sys
import analytical

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_NAME = os.environ['PROJECT_NAME']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = eval(os.environ['DJANGO_ISNOT_PRODUCTION'])

ALLOWED_HOSTS = ['{0}'.format(i) for i in os.environ['ALLOWED_HOSTS'].split(' ')]

# INTERNAL_IPS = ['corporalocal.nz', 'corporalocal.io', 'dev.koreromaori.com', '10.1.160.139', '127.0.0.1']

# For ELB Certificate & NGINX settings.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [

    'dal',
    'dal_select2',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'corpora',
    'corpus',
    'people',
    'license',
    'message',
    'transcription',
    'reo_api',

    'storages',
    'djangobower',

    'sekizai',
    'compressor',
    # 'compressor_toolkit',
    # 'sass_processor',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    'rest_framework',
    'rest_framework.authtoken',

    'analytical',
    'ckeditor',
    'ckeditor_uploader',

    'debug_toolbar',
]

MIDDLEWARE = [

    'debug_toolbar.middleware.DebugToolbarMiddleware',


    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware', # <= for caching entire site


    'django.middleware.locale.LocaleMiddleware',



    'corpora.middleware.LanguageMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware', # <= for caching entire site
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corpora.middleware.PersonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',

]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": 'corpora.middleware.show_toolbar_callback'
}


ROOT_URLCONF = 'corpora.urls'

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
                'django.template.context_processors.i18n',
                'sekizai.context_processors.sekizai',
                'license.context_processors.license',
                'corpora.context_processors.site',
            ],
        },
    },
]

WSGI_APPLICATION = 'corpora.wsgi.application'


# STORAGES #
DEFAULT_FILE_STORAGE =      os.environ['FILE_STORAGE']
AWS_ACCESS_KEY_ID =         os.environ['AWS_ID']
AWS_SECRET_ACCESS_KEY =     os.environ['AWS_SECRET']
AWS_STORAGE_BUCKET_NAME =   os.environ['AWS_BUCKET']
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = 'private'


# S3 only access
AWS_ACCESS_KEY_ID_S3 =         os.environ['AWS_ID_S3']
AWS_SECRET_ACCESS_KEY_S3 =     os.environ['AWS_SECRET_S3']


CKEDITOR_UPLOAD_PATH = "ckeditor_uploads/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# We use ansible to create the environment variables to use.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'], # TODO: Give this a better name?
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'], # TODO: Secure this!
        'HOST': os.environ['DATABASE_HOST'],           
        'PORT': '5432',
        }
    }

# All auth
AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)
LOGIN_REDIRECT_URL = 'people:profile'  # is there a more fool proof option?
ACCOUNT_ADAPTER = "people.adapter.PersonAccountAdapter"
SOCIALACCOUNT_ADAPTER = "people.adapter.PersonSocialAccountAdapter"
SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'], # Will require app approval for user_about_me access.
        'FIELDS': [ # see https://developers.facebook.com/docs/graph-api/reference/user/
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'locale',
            'timezone',
            'gender',
            'languages',
            'birthday'],
        #'LOCALE_FUNC': 'path.to.callable',
        'VERSION': 'v2.4'},
    'google':{
        'SCOPE': ['profile', 'email', 'https://www.googleapis.com/auth/plus.login'], # https://developers.google.com/identity/protocols/OAuth2
        'FIELDS': [ 
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'locale',
            'timezone',
            'gender',
            'languages',
            'birthday'],
    }
    }
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'

# These email settings should change for a production environment. Right now we're using G Suite.
# EMAIL_HOST=os.environ['EMAIL_HOST']
# EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']
# EMAIL_USE_SSL=True # move to deploy
# EMAIL_PORT=465 # Move to deploy

# Email
EMAIL_BACKEND = 'django_ses.SESBackend' # Use AWS Simple Email Service
AWS_SES_REGION_NAME = 'us-west-1'
AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
DEFAULT_FROM_EMAIL = u'"Kōrero Māori" <koreromaori@tehiku.nz>'


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

# Site ID
SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
TIME_ZONE = 'Pacific/Auckland'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ['STATIC_PATH'] #os.path.join(BASE_DIR, 'public', 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ['MEDIA_PATH']

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'corpora/static')

# BOWER IS DEPRICATED - FIND AN ALTERNATIVE!
BOWER_INSTALLED_APPS = {
    'jquery',
    'jquery-ui',
    'bootstrap',
    'opus-recorderjs#v4.1.4',
    'components-font-awesome#^4.7.0',
    'js-cookie',
    'popper.js',
    'chart.js',
    # 'fortawesome-font-awesome',
}

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, '...', 'static'),
# )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',

    # Additional finders
    'djangobower.finders.BowerFinder',
    # 'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',

)

memcache_server = os.environ['DJANGO_MEMCACHED_IP']
memcache_servers = []
for srv in memcache_server.split(','):
    srv = srv.strip()
    if srv != '':
        memcache_servers.append(
            "{0}:{1}".format(
                srv.strip(), os.environ['DJANGO_MEMCACHED_PORT']))

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': memcache_servers,
        'TIMEOUT': 300,
    }
}

# These may be required if caching the entire site.
# CACHE_MIDDLEWARE_ALIAS 
# CACHE_MIDDLEWARE_SECONDS
# CACHE_MIDDLEWARE_KEY_PREFIX


# DJANGO-COMPRESSOR SETTINGS
COMPRESS_PRECOMPILERS = (
    # ('text/coffeescript', 'coffee --compile --stdio'),
    # ('text/less', 'lessc {infile} {outfile}'),
    # ('text/x-sass', 'sass {infile} {outfile}'),
    # ('text/x-scss', 'sass --scss {infile} {outfile}'),
    # ('module', 'compressor_toolkit.precompilers.ES6Compiler'),
    ('text/x-scss', 'django_libsass.SassCompiler'),
    # ('text/stylus', 'stylus < {infile} > {outfile}'),
    # ('text/foobar', 'path.to.MyPrecompilerFilter'),
)
COMPRESS_LOCAL_NPM_INSTALL = False
# COMPRESS_ENABLED = True
# COMPRESS_NODE_MODULES = "/usr/local/lib/node_modules/"


'''
There are a set of settings that allow us to use CloudFront for s3 hosted
files. We also use a separate bucket for static files, because Corpora
needs protected s3 files (e.g. recordings).
'''
if os.environ['ENVIRONMENT_TYPE'] != 'local':
    AWS_STATIC_BUCKET_NAME = os.environ['AWS_STATIC_BUCKET']
    AWS_STATIC_DEFAULT_ACL = 'public-read'
    COMPRESS_URL = os.environ['AWS_CLOUDFRONT_DOMAIN']+'/'
    STATIC_URL = COMPRESS_URL
    COMPRESS_STORAGE = 'corpora.storage.CachedS3BotoStorage'
    STATICFILES_STORAGE = 'corpora.storage.CachedS3BotoStorage'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s -- %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
        'testconsole': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '../../logs/django.log',
            'formatter': 'verbose',
            'maxBytes': 1024 * 500,  # 500kb
            'backupCount': 10,
        },
        'celery': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '../../logs/celery.log',
            'formatter': 'simple',
            'maxBytes': 1024 * 500,  # 500 kb,
            'backupCount': 10,
        }
    },
    'loggers': {
        'django.test': {
            'handlers': ['testconsole'],
            'level': 'DEBUG',
            'propogate': True
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'corpora': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propogate': True
        },
        'celery': {
            'handlers': ['celery', 'console'],
            'level': 'DEBUG',
            'propogate': True
        }
    }
}


# API Stuff
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}


# CELERY #
# taken from
# https://github.com/celery/celery/blob/3.1/examples/django/proj/settings.py
# Celery settings
#             transport://userid:password@hostname:port/virtual_host
CELERY_BROKER_URL = 'amqp://%s:%s@%s:%s/%s' % (
    os.environ['CELERY_USER'],
    os.environ['CELERY_PASSWORD'],
    os.environ['CELERY_HOST'],
    os.environ['CELERY_PORT'],
    os.environ['CELERY_VHOST'])

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# two bottom properties are for logging,
# http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django
# CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERY_RESULT_BACKEND = 'cache+memcached://{0}/'.format(
    ';'.join(memcache_servers))

CELERY_TASK_RESULT_EXPIRES = 21600  # 6 hours.

### ERROS WITH UTC = FALSE!
# CELERY_TIMEZONE = TIME_ZONE
# CELERY_ENABLE_UTC = False


# DJANGO ANALYTICAL
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-114290321-1'
# GOOGLE_ANALYTICS_TRACKING_STYLE = \
#     analytical.templatetags.google_analytics.SCOPE_TRACK_MULTIPLE_DOMAINS
GOOGLE_ANALYTICS_DISPLAY_ADVERTISING = True
GOOGLE_ANALYTICS_SITE_SPEED = True
GOOGLE_ANALYTICS_ANONYMIZE_IP = True
FACEBOOK_PIXEL_ID = '158736294923584'
# INTERCOM_APP_ID =''


# Transcode API Stuff
TRANSCODE_API_TOKEN = os.environ['TRANSCODE_API_TOKEN']
