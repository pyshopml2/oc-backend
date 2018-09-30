from rest_framework import serializers

from document import models


class CatalogDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CatalogDocuments
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    catalog_documents_id = serializers.PrimaryKeyRelatedField(
        queryset=models.CatalogDocuments.objects.all(),
        source='catalog_documents',
        write_only=True,
        help_text='Catalog to which the'
                  ' document belongs (id) (not in get-request)'
    )

    class Meta:
        model = models.Document
        fields = '__all__'
        read_only_fields = ('catalog_documents',)
