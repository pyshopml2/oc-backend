from rest_framework import viewsets
from storage.models import *
from .serializers import *


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
