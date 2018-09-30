from rest_framework import routers

from . import viewsets

client_router = routers.SimpleRouter()
client_router.register(
    'status', viewsets.ClientStatusViewSet, base_name='client_status'
)
client_router.register('group', viewsets.ClientGroupViewSet, base_name='client_group')
client_router.register('', viewsets.ClientViewSet, base_name='client')

urlpatterns = client_router.urls
