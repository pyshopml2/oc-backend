from rest_framework import serializers
from storage.models import *

class StorageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'
