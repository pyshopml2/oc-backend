from task.models import *
from employee.models import Employee
from rest_framework import serializers

class TaskSerilizer(serializers.ModelSerializer):

    task_creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='task_creator', write_only=True)

    task_executor_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), source='task_executor', write_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        depth = 1


class TaskSSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        depth = 1