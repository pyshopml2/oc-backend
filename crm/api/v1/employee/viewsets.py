from rest_framework import viewsets
from employee.models import *
from .serializers import *

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerilizer

class GroupEmployeeViewSet(viewsets.ModelViewSet):
    queryset = GroupEmployee.objects.all()
    serializer_class = GroupEmployeeSerilizer