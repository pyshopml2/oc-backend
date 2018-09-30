from rest_framework import viewsets

from . import serializers
from position.models import Position


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
    serializer_class = serializers.PositionSerializer
