from task.models import *
from employee.models import Employee
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    task_creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='task_creator',
        write_only=True,
        help_text='Employee who created task (id) (not in get-request)'
    )

    task_executor_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='task_executor',
        write_only=True,
        help_text='Employee who must complete '
                  'the task (id) (not in get-request)'
    )

    class Meta:
        model = Task
        fields = '__all__'
        depth = 1
