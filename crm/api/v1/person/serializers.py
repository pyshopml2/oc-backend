from rest_framework import serializers
from person.models import *
from position.models import Position


class ContactPersonSerializer(serializers.ModelSerializer):
    """
    retrieve:
        Return a person instance.

    list:
        Return of all persons.

    create:
        Create a person.

    delete:
        Remove an existing person.

    partial_update:
        Update one or more fields.

    update:
        Update a person.
    """

    user_position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all(),
        source='user_position',
        write_only=True
    )

    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source='client',
        write_only=True
    )

    class Meta:
        model = ContactPerson
        fields = '__all__'
