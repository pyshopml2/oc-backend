from rest_framework import routers
from .viewsets import *

task_router = routers.SimpleRouter()

task_router.register('', TaskViewSet, base_name='task')