from rest_framework import routers
from .viewsets import *

employee_router = routers.SimpleRouter()

employee_router.register('employee', EmployeeViewSet)
employee_router.register('group', GroupEmployeeViewSet)