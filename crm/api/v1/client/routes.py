from rest_framework import routers
from .viewsets import *

client_router = routers.SimpleRouter()
client_router.register('status', ClientStatusViewSet, base_name='Client_Status')
client_router.register('group', ClientGroupViewSet, base_name='Client_Group')
client_router.register('', ClientViewSet, base_name='Client')

