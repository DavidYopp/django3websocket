"""
ASGI config for websocket_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from websocket_app.websocket import websocket_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_app.settings')

django_application = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'http':
        #let django handle the http request
        await django_application(scope, receive, send)
    elif scope['type'] == 'websocket':
        #handle websocket connection myself
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
