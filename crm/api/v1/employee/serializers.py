from rest_framework import serializers
from employee.models import *
from api.v1.position.serializers import PositionSerilizer
from api.v1.user.serializers import UserSerilizer
from api.v1.position.serializers import PositionSerilizer


class EmployeeSerializer(UserSerilizer):
    #employee_group = PositionSerilizer('employee_group')
    user_position = PositionSerilizer('user_position')
    class Meta(UserSerilizer.Meta):
        model = Employee
        fields = '__all__'
        depth = 2

class EmployeeGroupSerializer(serializers.ModelSerializer):
    creator = EmployeeSerializer('creator')
    class Meta:
        model = EmployeeGroup
        fields = '__all__'