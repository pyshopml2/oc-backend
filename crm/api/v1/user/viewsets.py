from .serializers import *
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return of all users.

    create:
        Create a user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields.

    update:
        Update a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
