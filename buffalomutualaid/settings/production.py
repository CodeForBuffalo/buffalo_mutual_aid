from .base import *
import os
import django_heroku

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

COMPRESS_OFFLINE = True

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
	
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = True

# Allow all host headers
ALLOWED_HOSTS = ['localhost','buffalomutualaid.herokuapp.com','buffalomutualaid.org']


try:
    from .local import *
except ImportError:
    pass
