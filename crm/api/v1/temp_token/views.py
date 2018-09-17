import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import *
from temp_token.models import TempToken
from core.tests.consts import DATE_TIME_TZ, TZ
from api.v1.user.serializers import UserSerializer

User = get_user_model()


class TempTokenView(APIView):

    def get(self, request, **kwargs):
        temp_token = kwargs.get('token')
        try:
            if self.check(temp_token):
                user = User.objects.get(
                    auth_temp_token__token=temp_token)
                token = user.auth_token
                user_serializer = UserSerializer(user)
                return Response(
                    user_serializer.data,
                    headers={'Authorization': 'Token ' + str(token)},
                    status=status.HTTP_200_OK)
            else:
                return Response('Token is not active or time expired')
        except User.DoesNotExist:
            return Response(data='User does not exist',
                            status=status.HTTP_400_BAD_REQUEST)
        except TempToken.DoesNotExist:
            return Response(data='Token does not exist',
                            status=status.HTTP_400_BAD_REQUEST)

    def check(self, temp_token):
        temp_token = TempToken.objects.get(token=temp_token)
        print(temp_token.active)
        print(datetime.datetime.now().strftime(DATE_TIME_TZ) <
                temp_token.expiration_date.strftime(DATE_TIME_TZ))
        if datetime.datetime.now().strftime(DATE_TIME_TZ) < \
                temp_token.expiration_date.strftime(DATE_TIME_TZ) \
                and temp_token.active:
            return True
        else:
            return False


temporary_auth_token = TempTokenView.as_view()
