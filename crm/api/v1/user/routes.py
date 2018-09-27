from rest_framework import routers

from .viewsets import *

user_router = routers.SimpleRouter()

user_router.register('', UserViewSet, base_name='user')
