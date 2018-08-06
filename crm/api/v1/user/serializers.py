from rest_framework import serializers
from user.models import Employee, User

class EmployeePositionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'