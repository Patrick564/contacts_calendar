import os
import dj_database_url

from dotenv import load_dotenv

load_dotenv()


# Database
DATABASES = {
    'default': {}
}

DATABASES['default'] = dj_database_url.config(
    default=os.getenv('DATABASE_URL'),
    conn_max_age=600
)
