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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            first_name = serializer.validated_data.get('first_name')
            middle_name = serializer.validated_data.get('middle_name')
            last_name = serializer.validated_data.get('last_name')
            ContactPerson.objects.create_user(email=email, first_name=first_name,
                                     middle_name=middle_name, last_name=last_name)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)
