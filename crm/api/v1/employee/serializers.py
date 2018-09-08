from typing import Dict

from rest_framework import serializers

from employee.models import *
from position.models import Position
from api.v1.user.serializers import UserSerializer
from api.v1.position.serializers import PositionSerializer


class EmployeeGroupSerializer(serializers.ModelSerializer):
    """
    retrieve:
        Return a group instance.

    list:
        Return of all groups.

    create:
        Create a group.

    delete:
        Remove an existing group.

    partial_update:
        Update one or more fields.

    update:
        Update a group.
    """

    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='creator',
        write_only=True
    )

    class Meta:
        model = EmployeeGroup
        fields = '__all__'
        read_only_fields = ('creator',)


class EmployeeSerializer(UserSerializer):
    """
    retrieve:
        Return a employee instance.

    list:
        Return of all employees.

    create:
        Create a employee.

    delete:
        Remove an existing employee.

    partial_update:
        Update one or more fields.

    update:
        Update a employee.
    """

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

    class Meta(UserSerializer.Meta):
        model = Employee
        fields = '__all__'
        read_only_fields = ('group',)
