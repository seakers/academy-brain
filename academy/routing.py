from django.urls import path
from academy_ws.consumers import AcademyConsumer


ws_routes = []
ws_routes.append(path('api/ws', AcademyConsumer.as_asgi()))