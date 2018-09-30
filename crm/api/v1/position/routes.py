from rest_framework import routers

from . import viewsets

position_router = routers.SimpleRouter()

position_router.register('', viewsets.PositionViewSet, base_name='position')
