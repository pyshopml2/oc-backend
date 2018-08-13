from rest_framework import viewsets
from person.models import *
from .serializers import *

class ContactPersonViewSet(viewsets.ModelViewSet):
    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerilizer
