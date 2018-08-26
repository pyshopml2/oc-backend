from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
import json
from .factories import CatalogDocumentsFactory


class BaseTestCase(APITestCase):

	def setUp(self):
		self.client = APIClient()
		self.catalog_documents = CatalogDocumentsFactory()

	def response_status_get(self, response):
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def response_status_post(self, response):
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def error(self, response):
		print(json.loads(response.content))
