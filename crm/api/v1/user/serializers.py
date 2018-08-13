from rest_framework import serializers
from user.models import *
from api.v1.position.serializers import PositionSerilizer

class UserSerilizer(serializers.ModelSerializer):
    #position_name = serializers.ReadOnlyField(source='user_position.name')
    position_name = PositionSerilizer(source='user_position')
    class Meta:
        model = User
        fields = '__all__'
