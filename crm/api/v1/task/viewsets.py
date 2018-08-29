from rest_framework import viewsets
from task.models import *
from .serializers import *


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerilizer


class OwnTasks(viewsets.ModelViewSet):
    serializer_class = TaskSerilizer

    def get_queryset(self):
        print(self.request.user)
        user = self.request.user
        return Task.objects.filter(task_executor=user)
