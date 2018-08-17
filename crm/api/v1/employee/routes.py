from rest_framework import routers
from .viewsets import *

employee_router = routers.SimpleRouter()

employee_router.register('group', EmployeeGroupViewSet)
employee_router.register('', EmployeeViewSet)
