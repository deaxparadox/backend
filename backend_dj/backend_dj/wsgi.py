"""
WSGI config for backend_dj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os


from django.core.wsgi import get_wsgi_application

import sconfig.config_file

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_dj.settings')
os.environ.get("DJANGO_SETTINGS_MODULE", 'backend_dj.settings')

application = get_wsgi_application()
