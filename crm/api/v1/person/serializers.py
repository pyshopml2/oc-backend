from rest_framework import serializers
from person.models import *
from api.v1.client.serializers import ClientSerializer
from api.v1.position.serializers import PositionSerilizer

class ContactPersonSerilizer(serializers.ModelSerializer):
    client = ClientSerializer('client')
    user_position = PositionSerilizer('user_position')
    class Meta:
        model = ContactPerson
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'user_position', 'date_of_birth',
                  'phone_number', 'extra_phone_number', 'other_contacts', 'timezone', 'is_active',
                  'is_staff', 'is_superuser', 'status', 'region', 'city', 'dialing_code', 'client']