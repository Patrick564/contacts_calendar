from dotenv import load_dotenv
load_dotenv()

import dj_database_url

from .base import *

# Turn off in production
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = ['.herokuapp.com', '*.herokuapp.*']


print(dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
    ))
# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
    )
}
