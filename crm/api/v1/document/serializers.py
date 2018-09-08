from rest_framework import serializers
from document.models import *


class CatalogDocumentsSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = CatalogDocuments
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
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

    catalog_documents_id = serializers.PrimaryKeyRelatedField(
        queryset=CatalogDocuments.objects.all(),
        source='catalog_documents',
        write_only=True
    )

    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('catalog_documents',)
