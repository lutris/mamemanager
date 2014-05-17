import os
from .base import *  # noqa

DEBUG = False

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mamemanager',
        'USER': 'mamemanager',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost'
    }
}
