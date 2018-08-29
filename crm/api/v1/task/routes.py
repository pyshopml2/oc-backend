from rest_framework import routers
from .viewsets import *

task_router = routers.SimpleRouter()

task_router.register('own', OwnTasks, base_name='own_tasks')
task_router.register('', TaskViewSet, base_name='task')
