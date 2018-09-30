from rest_framework import viewsets
from rest_framework.response import Response

from . import serializers
from client import models


class ClientStatusViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a status instance.

    list:
        Return of all statuses.

    create:
        Create a status.

    delete:
        Remove an existing status.

    partial_update:
        Update one or more fields.

    update:
        Update a status.
    """

    queryset = models.ClientStatus.objects.all()
    serializer_class = serializers.ClientStatusSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a client instance.

    list:
        Return of all clients.

    create:
        Create a client.

    delete:
        Remove an existing client.

    partial_update:
        Update one or more fields.

    update:
        Update a client.
    """

    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class ClientGroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a client group instance.

    list:
        Return of all groups.

    create:
        Create a client group.

    delete:
        Remove an existing group.

    partial_update:
        Update one or more fields.

    update:
        Update a group.
    """

    queryset = models.ClientGroup.objects.all()
    serializer_class = serializers.GroupClientSerializer
