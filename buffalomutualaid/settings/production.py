from .base import *
import os
import django_heroku

DEBUG = False

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'

django_heroku.settings(locals(), logging=False)

try:
    from .local import *
except ImportError:
    pass
