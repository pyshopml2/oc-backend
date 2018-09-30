from rest_framework import routers

from . import viewsets

person_router = routers.SimpleRouter()

person_router.register('', viewsets.ContactPersonViewSet, base_name='person')
