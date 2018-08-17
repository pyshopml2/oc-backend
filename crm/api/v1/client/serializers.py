from rest_framework import serializers
from client.models import *
from api.v1.employee.serializers import EmployeeSerializer

class ClientStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClientStatus
		fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
	employee_manager = EmployeeSerializer('employee_manager')
	contact_person = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	client_status = ClientStatusSerializer('client_status')
	employee_creator = EmployeeSerializer('employee_creator')
	#group_client = GroupClientSerializer
	class Meta:
		model = Client
		fields = '__all__'

class GroupClientSerializer(serializers.ModelSerializer):
	employee_creator = EmployeeSerializer('group_client')
	class Meta:
		model = ClientGroup
		fields = '__all__'