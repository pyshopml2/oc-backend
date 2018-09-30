import datetime

from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import factories
from ..models import Task
from core.tests.consts import *
from employee.tests.factories import EmployeeFactory

fake = Faker()


class TaskBaseTestCase(APITestCase):

    def setUp(self):
        self.employee = EmployeeFactory(
            first_name='Александр',
            middle_name='Сергеевич',
            last_name='Зубов',
            email='trelop@gmail.com',
            user_position=None,
            date_of_birth=datetime.datetime.today(),
            phone_number='9633609225',
            extra_phone_number='9633609225',
            other_contacts='Telegram - trelop',
            timezone='2018-08-29T20:43:18.869351+03:00',
            is_active=True,
            is_staff=True,
            is_superuser=False,
            status='1',
            login_skype='trelop',
            confirmed_email=True,
            group=None,
            password='password'
        )
        self.task = factories.TaskFactory(
            name='Task',
            creation_date='2018-08-29T20:43:18.869351+03:00',
            expiration_date='2018-08-29T20:43:18.869351+03:00',
            status='1',
            priority='1',
            task_description='Description',
            task_creator=self.employee,
            task_executor=self.employee
        )


class TaskTestCase(TaskBaseTestCase):

    def test_task_detail_get(self):
        url = reverse('task:task-detail', kwargs={'pk': self.task.pk})
        response = self.client.get(path=url)
        task = response.json()
        self.assertEqual(task['name'], self.task.name)
        self.assertEqual(task['creation_date'],
                         self.task.creation_date)

        self.assertEqual(task['expiration_date'], self.task.expiration_date)
        self.assertEqual(task['status'], self.task.status)
        self.assertEqual(task['priority'], self.task.priority)
        self.assertEqual(task['task_description'], self.task.task_description)
        self.assertEqual(task['task_creator']['id'], self.task.task_creator.pk)
        self.assertEqual(task['task_executor']['id'],
                         self.task.task_executor.pk)

    def test_task_list_get(self):
        url = reverse('task:task-list')
        response = self.client.get(path=url)
        task = response.json()[0]
        self.assertEqual(task['name'], self.task.name)
        self.assertEqual(task['creation_date'],
                         self.task.creation_date)

        self.assertEqual(task['expiration_date'], self.task.expiration_date)
        self.assertEqual(task['status'], self.task.status)
        self.assertEqual(task['priority'], self.task.priority)
        self.assertEqual(task['task_description'], self.task.task_description)
        self.assertEqual(task['task_creator']['id'], self.task.task_creator.pk)
        self.assertEqual(task['task_executor']['id'],
                         self.task.task_executor.pk)

    def test_task_post(self):
        url = reverse('task:task-list')
        data = {
            'name': 'Name',
            'creation_date': datetime.datetime.now(tz=TZ),
            'expiration_date': datetime.datetime.now(tz=TZ),
            'status': '1',
            'priority': '1',
            'task_description': 'Description',
            'task_creator_id': self.employee.pk,
            'task_executor_id': self.employee.pk,
        }
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        task_id = response.json().get('id')

        self.assertTrue(Task.objects.filter(pk=task_id).exists())

        task = Task.objects.get(pk=task_id)

        self.assertEqual(task.name, data['name'])
        self.assertEqual(task.creation_date, data['creation_date'])
        self.assertEqual(task.expiration_date, data['expiration_date'])
        self.assertEqual(task.status, data['status'])
        self.assertEqual(task.priority, data['priority'])
        self.assertEqual(task.task_description, data['task_description'])
        self.assertEqual(task.task_creator.pk, data['task_creator_id'])
        self.assertEqual(task.task_executor.pk, data['task_executor_id'])
