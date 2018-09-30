from rest_framework import routers

from . import viewsets

storage_router = routers.SimpleRouter()

storage_router.register('', viewsets.StorageViewSet, base_name='storage')
