from rest_framework import viewsets
from storage.models import *
from .serializers import *


class StorageViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a storage instance.

    list:
        Return of all storages.

    create:
        Create a storage.

    delete:
        Remove an existing storage.

    partial_update:
        Update one or more fields.

    update:
        Update a storage.
    """

    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
