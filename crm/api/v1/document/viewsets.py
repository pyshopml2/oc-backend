from rest_framework import viewsets
from document.models import *
from .serializers import *

class CatalogDocumentsViewSet(viewsets.ModelViewSet):
    queryset = CatalogDocuments.objects.all()
    serializer_class = CatalogDocumentsSerilizer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerilizer