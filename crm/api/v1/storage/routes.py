from rest_framework import routers
from .viewsets import *

storage_router = routers.SimpleRouter()

storage_router.register('', StorageViewSet, base_name='storage')
