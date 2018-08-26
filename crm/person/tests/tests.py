from django.urls import reverse

from core.tests.base import BaseTestCase
from .factories import *
from client.models import *
import json

class EmployeeTestCase(BaseTestCase):

	def test_employee_list_get(self):
		response = self.client.get(reverse('Employee:employee-list'))
		self.response_status_get(response)

	def test_employee_post(self):
		data = {
			'first_name': 'Венедикт',
			'middle_name': 'Сергеевич',
			'last_name': 'Азимов',
			'email': 'azimov@gmail.com',
			'date_of_birth': '1967-09-12',
			'phone_number': '9633609225',
			'extra_phone_number': '9633609224',
			'other_contacts': 'Telegram - @io',
			'timezone': '2018-09-12T22:22:22',
			'is_active': True,
			'is_staff': True,
			'is_superuser': True,
			'status': '1',
			'login_skype': 'io',
			'confirmed_email': True,
			'password': 'password',
		}
		url = reverse('Employee:employee-list')
		response = self.client.post(url, data)
		self.error(response)
		self.response_status_post(response)

	def test_employee_group_list_get(self):
		response = self.client.get(reverse('Employee:employee_group-list'))
		self.response_status_get(response)

	def test_employee_group_post(self):
		employee_group_data = EmployeeGroupFactory()
		data = {
			'name': 'Группа клиентов',
			'description': 'Описание данной группы',
		}
		url = reverse('Employee:employee_group-list')
		response = self.client.post(url, data)
		self.response_status_post(response)

