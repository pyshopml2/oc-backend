from rest_framework import serializers

from temp_token.models import TempToken


class TempTokenSerializer(serializers.Serializer):
    class Meta:
        model = TempToken
        fields = '__all__'
