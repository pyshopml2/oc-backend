from rest_framework import routers

from .viewsets import *

client_router = routers.SimpleRouter()
client_router.register(
    'status', ClientStatusViewSet, base_name='client_status'
)
client_router.register('group', ClientGroupViewSet, base_name='client_group')
client_router.register('', ClientViewSet, base_name='client')

urlpatterns = client_router.urls
