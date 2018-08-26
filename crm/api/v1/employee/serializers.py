from rest_framework import serializers
from employee.models import *
from api.v1.position.serializers import PositionSerilizer
from api.v1.user.serializers import UserSerilizer
from api.v1.position.serializers import PositionSerilizer
from position.models import Position


class EmployeeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeGroup
        fields = '__all__'


class EmployeeSerializer(UserSerilizer):

    user_position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(), source='user_position', write_only=True)



    class Meta(UserSerilizer.Meta):
        model = Employee
        fields = '__all__'
        read_only_fields = ('group',)
        depth = 1
