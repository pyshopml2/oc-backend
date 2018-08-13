from rest_framework import serializers
from employee.models import *

class EmployeeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class GroupEmployeeSerilizer(serializers.ModelSerializer):
    employee_group = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = GroupEmployee
        fields = '__all__'