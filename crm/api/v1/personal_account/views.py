from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from task.models import Task
from client.models import Client
from employee.models import Employee
from api.v1.task.serializers import TaskSerializer
from api.v1.client.serializers import ClientSerializer
from api.v1.employee.serializers import EmployeeSerializer


class PersonalAccountViewSet(views.APIView):

    authentication_classes = (SessionAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        client_queryset = Client.objects.filter(
            employee_manager=request.user)
        task_queryset = Task.objects.filter(
            task_executor=request.user)

        tasks = TaskSerializer(task_queryset, many=True)
        clients = ClientSerializer(client_queryset, many=True)

        employees = EmployeeSerializer(
            Employee.objects.all(), many=True)

        return Response({
            'clients': clients.data,
            'tasks': tasks.data,
            'employees': employees.data,
        })


personal_account = PersonalAccountViewSet.as_view()
