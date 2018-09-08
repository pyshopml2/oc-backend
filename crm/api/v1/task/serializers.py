from task.models import *
from employee.models import Employee
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    """
    retrieve:
        Return a task instance.

    list:
        Return of all tasks.

    create:
        Create a task.

    delete:
        Remove an existing task.

    partial_update:
        Update one or more fields.

    update:
        Update a task.
    """

    task_creator_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='task_creator',
        write_only=True
    )

    task_executor_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        source='task_executor',
        write_only=True
    )

    class Meta:
        model = Task
        fields = '__all__'
        depth = 1
