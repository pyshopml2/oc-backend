import datetime

from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import *

fake = Faker()


class TaskBaseTestCase(APITestCase):

	def setUp(self):
		self.storage = StorageFactory()


class TaskTestCase(TaskBaseTestCase):

	def test_storage_detail_get(self):
		url = reverse('storage:storage-detail', kwargs={'pk': self.storage.pk})
		response = self.client.get(path=url)
		storage = response.json()
		self.assertEqual(storage['name'], self.storage.name)
		self.assertEqual(storage['address'], self.storage.address)
		self.assertEqual(storage['mode'], self.storage.mode)
		self.assertEqual(storage['first_name'], self.storage.first_name)
		self.assertEqual(storage['middle_name'], self.storage.middle_name)
		self.assertEqual(storage['last_name'], self.storage.last_name)
		self.assertEqual(storage['phone_number'], self.storage.phone_number)
		# self.assertEqual(storage['scheme'], self.storage.scheme)
		self.assertEqual(storage['note'], self.storage.note)

	def test_storage_list_get(self):
		url = reverse('storage:storage-list')
		response = self.client.get(path=url)
		storage = response.json()[0]
		self.assertEqual(storage['name'], self.storage.name)
		self.assertEqual(storage['address'], self.storage.address)
		self.assertEqual(storage['mode'], self.storage.mode)
		self.assertEqual(storage['first_name'], self.storage.first_name)
		self.assertEqual(storage['middle_name'], self.storage.middle_name)
		self.assertEqual(storage['last_name'], self.storage.last_name)
		self.assertEqual(storage['phone_number'], self.storage.phone_number)
		# self.assertEqual(storage['scheme'], self.storage.scheme)
		self.assertEqual(storage['note'], self.storage.note)

	def test_storage_post(self):
		url = reverse('client:client_status-list')
		data = {
			'name': 'Склад №2',
			'address': 'Республика КОми',
			'mode': 'Пн-Пт',
			'first_name': 'Антон',
			'middle_name': 'Сергеевич',
			'last_name': 'Хозяинов',
			'phone_number': '9633609225',
			# 'scheme': self.storage.scheme,
		}
		response = self.client.post(path=url, data=data)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		storage_id = response.json().get('id')

		self.assertTrue(Storage.objects.filter(pk=storage_id).exists())

		storage = Storage.objects.get(pk=storage_id)

		self.assertEqual(storage.name, data['name'])
		self.assertEqual(storage.address, data['address'])
		self.assertEqual(storage.mode, data['mode'])
		self.assertEqual(storage.first_name, data['first_name'])
		self.assertEqual(storage.middle_name, data['middle_name'])
		self.assertEqual(storage.last_name, data['last_name'])
		self.assertEqual(storage.phone_number, data['phone_number'])
		self.assertEqual(storage.scheme, self.storage.scheme)