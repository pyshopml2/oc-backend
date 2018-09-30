from rest_framework import serializers

from storage.models import Storage


class StorageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storage
        fields = '__all__'
