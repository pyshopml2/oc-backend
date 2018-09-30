from rest_framework import serializers

from api.v1.user import serializers as user_serializer
from client.models import Client
from person.models import ContactPerson
from position.models import Position


class ContactPersonSerializer(user_serializer.UserSerializer):
    user_position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(),
        source='user_position',
        write_only=True,
        help_text='Position person (id) (not in get-request)'
    )

    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source='client',
        write_only=True,
        help_text='Client (id) (not in get-request)'
    )

    class Meta:
        model = ContactPerson
        fields = '__all__'
