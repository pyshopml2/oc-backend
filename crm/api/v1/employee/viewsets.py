from rest_framework import viewsets, status
from rest_framework.response import Response

from employee.models import Employee, EmployeeGroup
from .serializers import EmployeeSerializer, \
    EmployeeGroupSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a employee instance.

    list:
        Return of all employees.

    create:
        Create a employee.

    delete:
        Remove an existing employee.

    partial_update:
        Update one or more fields.

    update:
        Update a employee.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            first_name = serializer.validated_data.get('first_name')
            middle_name = serializer.validated_data.get('middle_name')
            last_name = serializer.validated_data.get('last_name')
            Employee.objects.create_user(email=email, first_name=first_name,
                                         middle_name=middle_name, last_name=last_name)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)


class EmployeeGroupViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a group instance.

    list:
        Return of all groups.

    create:
        Create a group.

    delete:
        Remove an existing group.

    partial_update:
        Update one or more fields.

    update:
        Update a group.
    """

    queryset = EmployeeGroup.objects.all()
    serializer_class = EmployeeGroupSerializer
