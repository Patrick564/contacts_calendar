import os
import dj_database_url
from dotenv import load_dotenv
load_dotenv()

from .base import *

# Turn off in production
DEBUG = False

# Generate if is a new project
SECRET_KEY = os.getenv('SECRET_KEY')

# Production checks
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Sendgrid API key
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')

# Allowed hosts
ALLOWED_HOSTS = ['*']
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RAILWAY_STATIC_URL')

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600
    )
}
