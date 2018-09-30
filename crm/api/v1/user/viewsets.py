from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response

from . import serializers

User = get_user_model()


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
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            first_name = serializer.validated_data.get('first_name')
            middle_name = serializer.validated_data.get('middle_name')
            last_name = serializer.validated_data.get('last_name')
            User.objects.create_user(email=email, first_name=first_name,
                                     middle_name=middle_name, last_name=last_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)

