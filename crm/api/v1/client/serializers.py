from rest_framework import serializers

from person.models import ContactPerson
from employee.models import Employee
from client.models import ClientStatus, ClientGroup, Client


class ClientStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientStatus
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
        queryset=ClientStatus.objects.all(),
        source='client_status',
        write_only=True,
        help_text='Status client (id) (not in get-request)'
    )

    client_group_id = serializers.PrimaryKeyRelatedField(
        queryset=ClientGroup.objects.all(),
        source='client_group',
        write_only=True,
        many=True,
        help_text='Client group (id) (not in get-request)'
    )

    class Meta:
        model = Client
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
        model = ClientGroup
        fields = '__all__'
