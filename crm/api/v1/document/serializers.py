from rest_framework import serializers
from document.models import *

class CatalogDocumentsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CatalogDocuments
        fields = '__all__'

class DocumentSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'