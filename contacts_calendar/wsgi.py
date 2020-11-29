"""
WSGI config for contacts_calendar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

load_dotenv()


if os.getenv('PRODUCTION'):
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'contacts_calendar.settings.production'
    )
else:
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'contacts_calendar.settings.local'
    )

application = get_wsgi_application()
