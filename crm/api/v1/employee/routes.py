from rest_framework import routers

from . import viewsets

employee_router = routers.SimpleRouter()

employee_router.register(
    'group', viewsets.EmployeeGroupViewSet, base_name='employee_group'
)
employee_router.register('', viewsets.EmployeeViewSet, base_name='employee')
