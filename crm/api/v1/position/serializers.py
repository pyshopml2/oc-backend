from rest_framework import serializers
from position.models import *
from user.models import User


class PositionSerializer(serializers.ModelSerializer):
    """
    retrieve:
        Return a position instance.

    list:
        Return of all positions.

    create:
        Create a position.

    delete:
        Remove an existing position.

    partial_update:
        Update one or more fields.

    update:
        Update a position.
    """

    user_position = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Position
        fields = '__all__'
