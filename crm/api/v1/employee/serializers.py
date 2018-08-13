from rest_framework import serializers
from employee.models import *
from api.v1.position.serializers import PositionSerilizer


class EmployeeSerializer(serializers.ModelSerializer):
    #employee_group = PositionSerilizer('employee_group')
    user_position = PositionSerilizer('user_position')
    class Meta:
        model = Employee
        fields = '__all__'

class GroupEmployeeSerializer(serializers.ModelSerializer):
    creator = EmployeeSerializer('creator')
    class Meta:
        model = GroupEmployee
        fields = '__all__'