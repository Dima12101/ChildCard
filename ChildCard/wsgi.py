"""
WSGI config for ChildCard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

sys.path.insert(0, '/opt/python/current/app')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ChildCard.settings'

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChildCard.settings')
application = get_wsgi_application()
