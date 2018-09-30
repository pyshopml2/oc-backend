import datetime

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt import tokens
from rest_framework.views import APIView

from api.v1.user.serializers import UserSerializer
from core.tests.consts import DATE_TIME_TZ
from temp_token.models import TempToken

User = get_user_model()


class TempTokenView(APIView):
    def get(self, request, *args, **kwargs):
        temp_token = kwargs.get('token')
        try:
            if self.check_availability(temp_token):
                user = User.objects.get(
                    auth_temp_token__token=temp_token)
                refresh_token = tokens.RefreshToken.for_user(user)
                access_token = tokens.AccessToken.for_user(user)
                user_serializer = UserSerializer(user)
                return Response(
                    user_serializer.data,
                    headers={'refresh': refresh_token, 'access': access_token},
                    status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Token is not active or time expired'},
                                status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(data={'detail': 'User does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)
        except TempToken.DoesNotExist:
            return Response(data={'detail': 'Token is invalid'},
                            status=status.HTTP_400_BAD_REQUEST)

    def check_availability(self, temp_token):
        temp_token = TempToken.objects.get(token=temp_token)
        if datetime.datetime.now().strftime(DATE_TIME_TZ) < \
                temp_token.expiration_date.strftime(DATE_TIME_TZ) \
                and temp_token.active:
            temp_token.active = False
            temp_token.save()
            return True
        else:
            return False
