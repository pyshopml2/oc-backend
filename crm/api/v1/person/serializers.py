from rest_framework import serializers
from api.v1.user.serializers import UserSerializer

from person.models import *
from position.models import Position


class ContactPersonSerializer(UserSerializer):
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
