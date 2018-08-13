from rest_framework import viewsets
from task.models import *
from .serializers import *

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerilizer