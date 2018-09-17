from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, \
    SessionAuthentication

from task.models import *
from .serializers import *


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
    serializer_class = TaskSerializer
