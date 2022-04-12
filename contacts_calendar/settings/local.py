import os
from dotenv import load_dotenv
load_dotenv()

from .base import *

# Secret key
SECRET_KEY = os.getenv('SECRET_KEY')

# Turn off in production
DEBUG = True

# Don't let this in production
ALLOWED_HOSTS = ['*']

# Sendgrid API key
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME_DB'),
        'USER': os.getenv('USER_DB'),
        'PASSWORD': os.getenv('PASSWORD_DB'),
        'HOST': os.getenv('HOST_DB'),
        'PORT': os.getenv('PORT_DB')
    }
}
