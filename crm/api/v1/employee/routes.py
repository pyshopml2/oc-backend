from rest_framework import routers
from .viewsets import *

employee_router = routers.SimpleRouter()

employee_router.register('group', EmployeeGroupViewSet, base_name='employee_group')
employee_router.register('', EmployeeViewSet, base_name='employee')
