from django.urls import reverse
from rest_framework import status
from employee.models import Employee
from rest_framework.test import APITestCase


class AuthTestCase(APITestCase):

    def test_own_task_get(self):
        password = 'Password'
        employee = Employee.objects.create_user(
            email='email@new.employee',
            password=password
        )
        url = reverse('token')
        data = {
            'email': employee.email,
            'password': password,
        }
        response = self.client.post(path=url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'token')
