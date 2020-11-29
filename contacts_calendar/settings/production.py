import os
import dj_database_url

from dotenv import load_dotenv
from .base import *

load_dotenv()


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

DATABASES['default'] = dj_database_url.config(
    default=os.getenv('DATABASE_URL')
)
