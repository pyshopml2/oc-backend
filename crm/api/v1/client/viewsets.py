from rest_framework import viewsets
from client.models import *
from .serializers import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema



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

    queryset = ClientStatus.objects.all()
    serializer_class = ClientStatusSerializer


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
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    # @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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
    queryset = ClientGroup.objects.all()
    serializer_class = GroupClientSerializer
