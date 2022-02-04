from dotenv import load_dotenv
load_dotenv()

import dj_database_url

from .base import *

# Turn off in production
DEBUG = False

# Allowed hosts
ALLOWED_HOSTS = ['.herokuapp.com', '*.herokuapp.*']

# Database
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
