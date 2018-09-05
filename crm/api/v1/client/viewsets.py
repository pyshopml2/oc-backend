from rest_framework import viewsets
from client.models import *
from .serializers import *


class ClientStatusViewSet(viewsets.ModelViewSet):
    queryset = ClientStatus.objects.all()
    serializer_class = ClientStatusSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientGroupViewSet(viewsets.ModelViewSet):
    queryset = ClientGroup.objects.all()
    serializer_class = GroupClientSerializer
