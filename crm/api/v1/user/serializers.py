from rest_framework import serializers
from user.models import *
from api.v1.position.serializers import PositionSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    retrieve:
        Return a user instance.

    list:
        Return of all users.

    create:
        Create a user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields.

    update:
        Update a user.
    """

    # position_name = serializers.ReadOnlyField(source='user_position.name')
    # position_name = PositionSerilizer(source='user_position')
    class Meta:
        model = User
        fields = '__all__'
        depth = 1
