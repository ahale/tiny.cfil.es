# -*- coding: utf-8 -*-

BASE_URL = 'http://tiny.cfil.es'

PREFIX = ''

DEBUG = True
TESTING = False

SECRET_KEY = 'alohamoonshine'
CSRF_ENABLED = True
CSRF_SESSION_KEY = '_csrf_token'

SQLALCHEMY_DATABASE_URI = 'sqlite:///shorty.sqlite'

try:
    from .local_settings import *
except ImportError:
    pass
