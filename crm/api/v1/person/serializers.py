from rest_framework import serializers
from person.models import *
from position.models import Position

class ContactPersonSerilizer(serializers.ModelSerializer):

    user_position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(), source='user_position', write_only=True)

    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), source='client', write_only=True)

    class Meta:
        model = ContactPerson
        fields = '__all__'