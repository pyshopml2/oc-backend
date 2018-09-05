import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from .factories import *
from core.tests.consts import *
from document.models import Document, CatalogDocuments


class DocumentBaseTestCase(APITestCase):

    def setUp(self):
        self.catalog_documents = CatalogDocumentsFactory()
        self.document = DocumentFactory(
            catalog_documents=self.catalog_documents,
            status='1',
            created_date='2018-08-29T20:43:18.869351+03:00'
        )


class DocumentTestCase(DocumentBaseTestCase):

    def test_document_detail_get(self):
        response = self.client.get(
            reverse('document:document-detail',
                    kwargs={'pk': self.document.pk}))
        document_id = response.json().get('id')

        self.assertTrue(Document.objects.filter(pk=document_id).exists())

        document = Document.objects.get(pk=document_id)

        self.assertEqual(document.status, self.document.status)
        self.assertEqual(document.created_date, self.document.created_date)
        self.assertEqual(document.catalog_documents.pk,
                         self.document.catalog_documents.pk)

    def test_document_list_get(self):
        response = self.client.get(reverse('document:document-list'))
        document_id = response.json()[0].get('id')

        self.assertTrue(Document.objects.filter(pk=document_id).exists())

        document = Document.objects.get(pk=document_id)

        self.assertEqual(document.status, self.document.status)
        self.assertEqual(document.created_date, self.document.created_date)
        self.assertEqual(document.catalog_documents.pk,
                         self.document.catalog_documents.pk)

    def test_document_post(self):
        url = reverse('document:document-list')
        data = {
            'catalog_documents_id': self.catalog_documents.pk,
            'status': '1',
            'created_date': datetime.datetime.now(tz=TZ)
        }
        response = self.client.post(path=url, data=data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED, response.data)

        document_id = response.json().get('id')

        self.assertTrue(Document.objects.filter(pk=document_id).exists())

        document = Document.objects.get(pk=document_id)

        self.assertEqual(document.status, data['status'])
        self.assertEqual(document.created_date.strftime(DATE),
                         data['created_date'].strftime(DATE))

        self.assertEqual(document.catalog_documents.pk,
                         data['catalog_documents_id'])


class CatalogDocumentTestCase(DocumentBaseTestCase):

    def test_catalog_documents_detail_get(self):
        response = self.client.get(
            reverse('document:catalog-detail',
                    kwargs={'pk': self.catalog_documents.pk}))
        catalog_id = response.json().get('id')

        self.assertTrue(Document.objects.filter(pk=catalog_id).exists())

        catalog_documents = CatalogDocuments.objects.get(pk=catalog_id)

        self.assertEqual(catalog_documents.description,
                         self.catalog_documents.description)

        self.assertEqual(catalog_documents.name, self.catalog_documents.name)

    def test_catalog_documents_list_get(self):
        response = self.client.get(reverse('document:catalog-list'))
        catalog_documents = response.json()[0]

        self.assertEqual(catalog_documents['description'],
                         self.catalog_documents.description)

        self.assertEqual(catalog_documents['name'],
                         self.catalog_documents.name)

    def test_catalog_documents_detail_post(self):
        url = reverse('document:catalog-list')
        data = {
            'name': 'Document',
            'description': 'Description',
        }
        response = self.client.post(path=url, data=data, format='json')
        catalog_id = response.json().get('id')

        self.assertTrue(
            CatalogDocuments.objects.filter(pk=catalog_id).exists())

        catalog_documents = CatalogDocuments.objects.get(pk=catalog_id)

        self.assertEqual(catalog_documents.name, data['name'])
        self.assertEqual(catalog_documents.description, data['description'])
