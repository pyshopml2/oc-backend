from rest_framework import routers

from .viewsets import *

position_router = routers.SimpleRouter()

position_router.register('', PositionViewSet, base_name='position')
