from rest_framework import serializers
from task.models import *

class TaskSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
