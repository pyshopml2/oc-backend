from rest_framework import serializers
from user.models import *
from api.v1.position.serializers import PositionSerializer
from temp_token.models import TempToken


class TempTokenSerializer(serializers.Serializer):
    class Meta:
        model = TempToken
        fields = '__all__'
