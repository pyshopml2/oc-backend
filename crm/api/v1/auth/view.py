import datetime

from rest_framework import status
from rest_framework.views import APIView
from .serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class ObtainAuthToken(APIView):
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


obtain_auth_token = ObtainAuthToken.as_view()
