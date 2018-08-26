from rest_framework.test import APITestCase
from rest_framework import status
import json
from client.models import *
from employee.tests.factories import *
from rest_framework.test import APIClient
from client.tests.factories import *
from django.core import serializers

class BaseTestCase(APITestCase):

	def setUp(self):
		self.client = APIClient()

	def response_status_get(self, response):
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def response_status_post(self, response):
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def error(self, response):
		print(json.loads(response.content))
