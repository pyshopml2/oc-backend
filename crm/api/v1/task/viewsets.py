from rest_framework import viewsets

from task.models import Task
from . import serializers


class TaskViewSet(viewsets.ModelViewSet):
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

    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
