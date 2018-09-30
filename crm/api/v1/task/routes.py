from rest_framework import routers

from . import viewsets

task_router = routers.SimpleRouter()

task_router.register('', viewsets.TaskViewSet, base_name='task')
