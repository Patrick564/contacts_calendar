import dj_database_url

from dotenv import load_dotenv
load_dotenv()

from .base import *

# Turn off in production
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = ['*.herokuapp.com']

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600
    )}
