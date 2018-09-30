from rest_framework import viewsets

from . import serializers
from document import models


class CatalogDocumentsViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a catalog instance.

    list:
        Return of all catalog documents.

    create:
        Create a catalogs.

    delete:
        Remove an existing catalogs.

    partial_update:
        Update one or more fields.

    update:
        Update a catalog.
    """

    queryset = models.CatalogDocuments.objects.all()
    serializer_class = serializers.CatalogDocumentsSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a document instance.

    list:
        Return of all document.

    create:
        Create a document.

    delete:
        Remove an existing document.

    partial_update:
        Update one or more fields.

    update:
        Update a document.
    """

    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
