from rest_framework import routers
from .viewsets import UserViewSet, EmployeeViewSet

api_router = routers.SimpleRouter()
api_router.register('user', UserViewSet)
api_router.register('employee', EmployeeViewSet)