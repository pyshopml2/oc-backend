from rest_framework import routers

from . import viewsets

user_router = routers.SimpleRouter()

user_router.register('', viewsets.UserViewSet, base_name='user')
