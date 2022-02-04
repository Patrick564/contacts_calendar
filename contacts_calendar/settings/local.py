from dotenv import load_dotenv
load_dotenv()

from .base import *

# Turn off in production
DEBUG = True

# Don't let this in production
ALLOWED_HOSTS = ['*']

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
