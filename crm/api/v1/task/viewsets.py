from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, \
    SessionAuthentication

from task.models import *
from .serializers import *


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerilizer


class OwnTasks(ListAPIView):
    serializer_class = TaskSerilizer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        tasks = Task.objects.filter(task_executor=self.request.user)
        return tasks
