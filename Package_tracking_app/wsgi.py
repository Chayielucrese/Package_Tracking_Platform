"""
WSGI config for Package_tracking_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Package_tracking_app.settings')
=======
os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'Package_tracking_app.settings')
>>>>>>> 93b4b2575ca0625f178face99cb5401f51dd5f25

application = get_wsgi_application()
