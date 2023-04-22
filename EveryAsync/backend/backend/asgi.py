import os 

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.dev")

djano_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": djano_asgi_app,
        # websocket routing to be implemented
    }
)

