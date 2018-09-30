from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import status, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from temp_token.models import EmailToken
from . import serializers

User = get_user_model()


class ResetPassword(APIView):
    """
    post:
        Update password
    ====================
    Required
    * User must be authorized
    * Password
    * Confirmed password

    # Expected data #
    ``` json
    {
        "password": [
            "qwerty12345"
        ],
        "confirmed_password": [
            "qwerty12345"
        ]
    }
    ```
    """

    serializer_class = serializers.ResetPasswordSerializer
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            users = User.objects.all()
            user = get_object_or_404(users, pk=request.user.pk)
            user.set_password(serializer.validated_data)
            user.save()
            return Response(
                serializer.validated_data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmEmail(APIView):
    """
    get:
        User must follow to link that confirm email address
    ==================================
    Required
    * Id user in ASCII format (base64)
    * Token
    """

    def get(self, request, **kwargs):
        encoded_id = kwargs.get('encoded_id')
        token = kwargs.get('token')
        try:
            user_id = force_text(urlsafe_base64_decode(encoded_id.encode()))
            user = User.objects.get(id=user_id)
            EmailToken.objects.get(user=user, token=token)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist, EmailToken.DoesNotExist):
            user = None

        if user is not None:
            user.confirmed_email = True
            user.save()
            return Response({'detail': 'Thank you for email confirmation.'})
        else:
            return Response({'detail': 'Email confirmation link is invalid!'})
