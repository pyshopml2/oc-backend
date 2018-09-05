from rest_framework import viewsets
from position.models import *
from .serializers import *


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerilizer
