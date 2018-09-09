from rest_framework import serializers
from position.models import *
from user.models import User


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'
