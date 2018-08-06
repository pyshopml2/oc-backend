from rest_framework import viewsets
from user.models import User, Employee
from .serializers import UserSerilizer, EmployeePositionSerilizer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerilizer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeePositionSerilizer
