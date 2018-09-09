from typing import Dict

from rest_framework import serializers

from employee.models import *
from position.models import Position
from api.v1.user.serializers import UserSerializer
from api.v1.position.serializers import PositionSerializer


class EmployeeGroupSerializer(serializers.ModelSerializer):
    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='creator',
        write_only=True,
        help_text='Employee who created group (id) (not in get-request)'
    )

    class Meta:
        model = EmployeeGroup
        fields = '__all__'
        read_only_fields = ('creator',)


class EmployeeSerializer(UserSerializer):
    user_position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(),
        source='user_position',
        write_only=True,
        help_text='Position employee (id) (not in get-request)'
    )

    group_id = serializers.PrimaryKeyRelatedField(
        queryset=EmployeeGroup.objects.all(),
        source='group',
        write_only=True,
        help_text='Employee group (id) (not in get-request)'
    )

    class Meta(UserSerializer.Meta):
        model = Employee
        fields = '__all__'
        read_only_fields = ('group',)
