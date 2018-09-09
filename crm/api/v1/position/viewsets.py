from rest_framework import viewsets
from position.models import *
from .serializers import *


class PositionViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a position instance.

    list:
        Return of all positions.

    create:
        Create a position.

    delete:
        Remove an existing position.

    partial_update:
        Update one or more fields.

    update:
        Update a position.
    """

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
