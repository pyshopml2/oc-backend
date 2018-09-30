from rest_framework import viewsets, status
from rest_framework.response import Response

from person.models import *
from .serializers import *


class ContactPersonViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a person instance.

    list:
        Return of all persons.

    create:
        Create a person.

    delete:
        Remove an existing person.

    partial_update:
        Update one or more fields.

    update:
        Update a person.
    """

    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
