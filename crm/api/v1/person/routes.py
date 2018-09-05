from rest_framework import routers
from .viewsets import *

person_router = routers.SimpleRouter()

person_router.register('', ContactPersonViewSet, base_name='person')
