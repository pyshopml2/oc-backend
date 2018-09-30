from rest_framework import viewsets

from . import serializers
from employee import models


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

    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


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

    queryset = models.EmployeeGroup.objects.all()
    serializer_class = serializers.EmployeeGroupSerializer
