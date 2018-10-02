from django.urls import reverse
from django.core.files.uploadedfile \
    import SimpleUploadedFile
from django.core.files import File
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from . import factories
from ..models import Storage


fake = Faker()


class TaskBaseTestCase(APITestCase):

    def setUp(self):
        self.storage = factories.StorageFactory()


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
        self.assertEqual(storage['scheme'],
                         'http://testserver/storage/1/' +
                         str(self.storage.scheme))

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
        self.assertEqual(storage['scheme'],
                         'http://testserver/storage/' +
                         str(self.storage.scheme))

        self.assertEqual(storage['note'], self.storage.note)

    def test_storage_post(self):
        url = reverse('storage:storage-list')
        data = File(open('tmp/trash/data.jpg', 'rb'))
        upload_file = SimpleUploadedFile(
            self.storage.scheme.name, data.read(), content_type='multipart')

        data = {
            'name': 'Склад №2',
            'address': 'Республика КОми',
            'mode': 'Пн-Пт',
            'first_name': 'Антон',
            'middle_name': 'Сергеевич',
            'last_name': 'Абрамов',
            'phone_number': '9633609225',
            'note': 'Записки',
            'scheme': upload_file
        }
        response = self.client.post(path=url, data=data, format='multipart')

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
        self.assertEqual(storage.scheme,
                         'tmp/img/' + str(data['scheme']))
