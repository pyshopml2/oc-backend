from rest_framework import serializers

from client import models
from employee.models import Employee


class ClientStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ClientStatus
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    employee_manager_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='employee_manager',
        write_only=True,
        help_text='Employee who work '
                  'with client (id) (not in get-request)'
    )

    employee_creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='employee_creator',
        write_only=True,
        help_text='Employee who created client (id) (not in get-request)'
    )

    client_status_id = serializers.PrimaryKeyRelatedField(
        queryset=models.ClientStatus.objects.all(),
        source='client_status',
        write_only=True,
        help_text='Status client (id) (not in get-request)'
    )

    client_group_id = serializers.PrimaryKeyRelatedField(
        queryset=models.ClientGroup.objects.all(),
        source='client_group',
        write_only=True,
        many=True,
        help_text='Client group (id) (not in get-request)'
    )

    class Meta:
        model = models.Client
        fields = '__all__'
        read_only_fields = (
            'employee_manager',
            'employee_creator',
            'client_status',
            'client_group'
        )
        depth = 1


class GroupClientSerializer(serializers.ModelSerializer):
    employee_creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='employee_creator',
        write_only=True,
        help_text='Employee who created group (id) (not in get-request)'
    )

    class Meta:
        model = models.ClientGroup
        fields = '__all__'
