from rest_framework import serializers
from position.models import *
from user.models import User

class PositionSerilizer(serializers.ModelSerializer):
    user_position = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Position
        fields = '__all__'