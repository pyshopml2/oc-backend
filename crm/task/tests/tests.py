import datetime

from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import *
from employee.tests.factories import EmployeeFactory

fake = Faker()

class TaskBaseTestCase(APITestCase):

	def setUp(self):
		self.task = TaskFactory()
		self.employee = EmployeeFactory()

class TaskTestCase(TaskBaseTestCase):

	def test_task_detail_get(self):
		url = reverse('task:task-detail', kwargs={'pk': self.task.pk})
		response = self.client.get(path=url)
		task = response.json()
		self.assertEqual(task['name'], self.task.name)
		# self.assertEqual(task['datetime_of_create'], self.task.datetime_of_create)
		# self.assertEqual(task['date_time_todo'], self.task.date_time_todo)
		self.assertEqual(task['status'], self.task.status)
		self.assertEqual(task['priority'], self.task.priority)
		self.assertEqual(task['task_description'], self.task.task_description)
		self.assertEqual(task['task_creator'], self.task.task_creator.pk)
		self.assertEqual(task['task_executor'], self.task.task_executor.pk)

	def test_task_list_get(self):
		url = reverse('task:task-list')
		response = self.client.get(path=url)
		task = response.json()[0]
		self.assertEqual(task['name'], self.task.name)
		# self.assertEqual(task['datetime_of_create'], self.task.datetime_of_create)
		# self.assertEqual(task['date_time_todo'], self.task.date_time_todo)
		self.assertEqual(task['status'], self.task.status)
		self.assertEqual(task['priority'], self.task.priority)
		self.assertEqual(task['task_description'], self.task.task_description)
		self.assertEqual(task['task_creator'], self.task.task_creator.pk)
		self.assertEqual(task['task_executor'], self.task.task_executor.pk)

	def test_client_status_post(self):
		url = reverse('client:client_status-list')
		data = {
			'name': 'Name',
			'datetime_of_create': datetime.datetime.now(),
			'date_time_todo': datetime.datetime.now(),
			'status': '1',
			'priority': '1',
			'task_description': 'Description',
			'task_creator': self.employee,
			'task_executor': self.employee,
		}
		response = self.client.post(path=url, data=data)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		task_id = response.json().get('id')

		self.assertTrue(Task.objects.filter(pk=task_id).exists())

		task = Task.objects.get(pk=task_id)

		self.assertEqual(task.name, self.task.name)
		self.assertEqual(task.datetime_of_create, self.task.datetime_of_create)
		self.assertEqual(task.date_time_todo, self.task.date_time_todo)
		self.assertEqual(task.status, self.task.status)
		self.assertEqual(task.priority, self.task.priority)
		self.assertEqual(task.task_description, self.task.task_description)
		self.assertEqual(task.task_creator.pk, self.task.task_creator.pk)
		self.assertEqual(task.task_executor.pk, self.task.task_executor.pk)
