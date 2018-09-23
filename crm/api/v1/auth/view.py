import datetime

from rest_framework import status
from rest_framework.views import APIView
from .serializers import ResetPasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import authentication

from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.http import HttpResponse

User = get_user_model()


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


class ConfirmEmail(APIView):
    """
    get:
        Confirm user email
    """

    def get(self, request, **kwargs):
        decoded = kwargs.get('decoded')
        try:
            user_id = force_text(urlsafe_base64_decode(decoded.encode()))
            user = User.objects.get(id=user_id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            return HttpResponse('User is not fouZnd')

        if user is not None:
            user.confirmed_email = True
            user.save()
            return HttpResponse('Thank you for your email confirmation.')
        else:
            return HttpResponse('Email confirmation link is invalid!')


confirm_email = ConfirmEmail.as_view()