from rest_framework import serializers
from document.models import *


class CatalogDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogDocuments
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    catalog_documents_id = serializers.PrimaryKeyRelatedField(
        queryset=CatalogDocuments.objects.all(),
        source='catalog_documents',
        write_only=True,
        help_text='Catalog to which the'
                  ' document belongs (id) (not in get-request)'
    )

    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('catalog_documents',)
