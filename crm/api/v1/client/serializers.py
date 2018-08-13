from rest_framework import serializers
from client.models import *

class ClientStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClientStatus
		fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class GroupClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = GroupClient
		fields = '__all__'