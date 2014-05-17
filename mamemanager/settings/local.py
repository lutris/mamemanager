from .base import *  # noqa

DEBUG = True

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mamemanager',
        'USER': 'mamemanager',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    }
}
