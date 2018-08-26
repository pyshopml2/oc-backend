from rest_framework import serializers
from document.models import *

class CatalogDocumentsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CatalogDocuments
        fields = '__all__'

class DocumentSerilizer(serializers.ModelSerializer):

    catalog_documents_id = serializers.PrimaryKeyRelatedField(
        queryset=CatalogDocuments.objects.all(), source='catalog_documents', write_only=True)

    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('catalog_documents',)