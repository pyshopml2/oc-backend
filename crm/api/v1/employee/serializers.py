from rest_framework import serializers

from api.v1.user import serializers as user_serializers
from employee import models
from position.models import Position


class EmployeeGroupSerializer(serializers.ModelSerializer):
    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Employee.objects.all(),
        source='creator',
        write_only=True,
        help_text='Employee who created group (id) (not in get-request)'
    )

    class Meta:
        model = models.EmployeeGroup
        fields = '__all__'
        read_only_fields = ('creator',)


class EmployeeSerializer(user_serializers.UserSerializer):
    user_position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(),
        source='user_position',
        write_only=True,
        help_text='Position employee (id) (not in get-request)'
    )

    group_id = serializers.PrimaryKeyRelatedField(
        queryset=models.EmployeeGroup.objects.all(),
        source='group',
        write_only=True,
        help_text='Employee group (id) (not in get-request)'
    )

    class Meta(user_serializers.UserSerializer.Meta):
        model = models.Employee
        fields = '__all__'
        read_only_fields = ('group',)
