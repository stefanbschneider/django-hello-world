""" Production Settings """
import os

# default: use settings from main settings.py if not overwritten
from .settings import *


DEBUG = False
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)
ALLOWED_HOSTS = ['django-hello-world-app.herokuapp.com']

# Activate Django-Heroku.
# django_heroku.settings(locals())

