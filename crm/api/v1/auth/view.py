import datetime

from rest_framework import status
from rest_framework.views import APIView
from .serializers import AuthTokenSerializer, \
    ResetPasswordSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import authentication

User = get_user_model()


class ObtainAuthToken(APIView):
    """
    post:
        Create new token
    """
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            token, created = Token.objects.get_or_create(
                user=serializer.validated_data['user']
            )

            if not created:
                token.created = datetime.datetime.utcnow()
                token.save()

            return Response({'token': token.key})
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


obtain_auth_token = ObtainAuthToken.as_view()


class ResetPassword(APIView):
    """
    post:
        Update password
    """

    serializer_class = ResetPasswordSerializer
    authentication_classes = (authentication.TokenAuthentication,
                              authentication.SessionAuthentication)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            users = User.objects.all()
            user = get_object_or_404(users, pk=request.user.pk)
            user.set_password(serializer.validated_data)
            user.save()
            return Response(
                serializer.validated_data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


reset_password = ResetPassword.as_view()
