import django_on_heroku
from descouple import config

from . base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOST = [
    'regencyO4.herokuapp.com',
    'regencyO4',
]

DEBUG_PROPAGATE_EXCEPTIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datafmt' : "%d/%b/%Y %H:%M:%S"
        }
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    }
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    }
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    }
}

# heroku Settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['options']['sslmode']