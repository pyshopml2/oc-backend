import datetime

from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import *

fake = Faker()


class PositionBaseTestCase(APITestCase):

	def setUp(self):
		self.position = PositionFactory()


class PositionTestCase(PositionBaseTestCase):

	def test_position_detail_get(self):
		url = reverse('position:position-detail', kwargs={'pk': self.position.pk})
		response = self.client.get(path=url)
		position = response.json()
		self.assertEqual(position['name'], self.position.name)
		self.assertEqual(position['description'], self.position.description)

	def test_position_list_get(self):
		url = reverse('position:position-list')
		response = self.client.get(path=url)
		position = response.json()[0]
		self.assertEqual(position['name'], self.position.name)
		self.assertEqual(position['description'], self.position.description)

	def test_position_post(self):
		url = reverse('position:position-list')
		data = {
			'name': 'Должность',
			'description': 'Описание должности'
		}
		response = self.client.post(path=url, data=data)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		position_id = response.json().get('id')

		self.assertTrue(Position.objects.filter(pk=position_id).exists())

		position = Position.objects.get(pk=position_id)

		self.assertEqual(position.name, data['name'])
		self.assertEqual(position.description, data['description'])

