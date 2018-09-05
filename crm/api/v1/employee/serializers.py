from typing import Dict

from rest_framework import serializers

from employee.models import *
from position.models import Position
from api.v1.user.serializers import UserSerilizer
from api.v1.position.serializers import PositionSerilizer


class EmployeeGroupSerializer(serializers.ModelSerializer):
    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='creator',
        write_only=True
    )

    class Meta:
        model = EmployeeGroup
        fields = '__all__'
        read_only_fields = ('creator',)


class EmployeeSerializer(UserSerilizer):
    user_position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(),
        source='user_position',
        write_only=True
    )

    group_id = serializers.PrimaryKeyRelatedField(
        queryset=EmployeeGroup.objects.all(),
        source='group',
        write_only=True
    )

    class Meta(UserSerilizer.Meta):
        model = Employee
        fields = '__all__'
        read_only_fields = ('group',)
