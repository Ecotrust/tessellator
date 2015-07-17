"""
Django settings for tessellator project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os
import warnings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CONFIG_FILE = os.path.normpath(os.path.join(BASE_DIR, 'config.ini'))
print CONFIG_FILE

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rpc4django',
    'api',
    'root',
)

class CORSMiddleware(object):
    """Always add CORS header to anything that comes back as JSON in the
    hackiest possible way
    """
    def process_response(self, request, response):
        if response.status_code != 200:
            return response
        if response.has_header('Content-type'):
            content_type = response['Content-type']
            if 'application/json' in content_type or 'application/javascript' in content_type:
                response['Access-Control-Allow-Origin'] = '*'
                if request.has_header('Access-Control-Request-Headers'):
                    response['Access-Control-Allow-Headers'] = request['Access-Control-Request-Headers']
        return response


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tessellator.settings.CORSMiddleware',
)

ROOT_URLCONF = 'tessellator.urls'

WSGI_APPLICATION = 'tessellator.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'fleeting-photons',
    # },
    # 'redis': {
    #     'BACKEND': 'redis_cache.RedisCache',
    #     'LOCATION': 'localhost:6379',
    #     'OPTIONS': {
    #         'DB': 1,
    #         'PARSER_CLASS': 'redis.connection.HiredisParser'
    #     },
    # },
# }

# Logging
# TODO: Move logging configuration into the ini file

from django.utils.log import DEFAULT_LOGGING
LOGGING = DEFAULT_LOGGING
LOGGING['handlers']['mail_admins']['include_html'] = True

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             # 'filename': '/home/point97/logs/user/django_tessellator001_debug.log',
#             'filename': 'debug.log'
#         },
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         '': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }



# TODO: Put the config parser into a P97.configuration module
from ConfigParser import RawConfigParser
class RawConfigParserWithDefaults(RawConfigParser):
    """RawConfigParser modified to have return a default value if something
    doesn't exist rather than throwing a NoSectionError.
    """ 
    def get(self, section, name, default=None):
        if self.has_option(section, name):
            return RawConfigParser.get(self, section, name)
        else:
            if default is None or self.has_section(section):
                warnings.warn('Configuration missing: %s.%s, defaulting to %s\n' % (section, name, default))
            return default
    
    def getlist(self, section, name):
        result = self.get(section, name)
        if not result:
            return []
        
        # parse a comma-separated string into a list of strings
        result = result.replace(' ', '')
        result = result.split(',')
        return result
        
    def getboolean(self, section, option, default=None):
        result = self.get(section, option, default)
        if type(result) is bool: 
            return result
        elif result.lower() in ('0', 'no', 'false'):
            return False
        elif result.lower() in ('1', 'yes', 'true'):
            return True
        else:
            warnings.warn('Configuration value %s.%s is not a boolean\n' % (section, name))
            return default

    def getint(self, section, option, default=None):
        result = self.get(section, option, default)
        try:
            return int(result)
        except ValueError:
            warnings.warn('Configuration value %s.%s is not an integer\n' % (section, name))
            return default

        
config = RawConfigParserWithDefaults()
config.read(CONFIG_FILE)

# Webapp config
# TODO: Maybe make a management command to generate a secret
SECRET_KEY = config.get('APP', 'SECRET_KEY', default='set secret key')
DEBUG = config.getboolean('APP', 'DEBUG', True)
TEMPLATE_DEBUG = config.getboolean('APP', 'TEMPLATE_DEBUG', True)
ALLOWED_HOSTS = config.getlist('APP', 'ALLOWED_HOSTS')

# MBTILES config
MBTILES_APP_CONFIG = dict(
    MBTILES_EXT=config.get('MBTILES', 'EXT', 'mbtiles'),
    MBTILES_ROOT=config.get('MBTILES', 'ROOT', '/tmp'),
    TILE_SIZE=config.getint('MBTILES', 'TILE_SIZE', 256),
    MISSING_TILE_404=config.getboolean('MBTILES', 'MISSING_TILE_404', True),
)

