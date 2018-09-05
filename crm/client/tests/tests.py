import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from core.tests.consts import *
from client.tests.factories import *
from employee.tests.factories import *


class ClientBaseTestCase(APITestCase):

    def setUp(self):
        self.api_client = APIClient()
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
            group=None
        )
        self.client_status = ClientStatusFactory(
            name='Status'
        )
        self.client_group = ClientGroupFactory(
            name='Name',
            description='Description',
            created_date='2018-08-29T20:43:18.869351+03:00',
            employee_creator=self.employee
        )
        self.client = ClientFactory(
            name='РАО «Харитонова»',
            other_names='РАО Аристотель',
            zip_code='184682',
            email='nikita1990@rao.edu',
            address='Россия, Ивановская область, проспект Ленина, дом 2',
            region='Ивановская область',
            city='Иваново',
            website='https://google.com',
            timezone='2018-08-29T20:43:18.869351+03:00',
            additional_info='Компания занимается добычей угля',
            note='Клиент также работает в странах СНГ',
            employee_manager=self.employee,
            client_status=self.client_status,
            employee_creator=self.employee,
            date_of_create=datetime.date.today(),
            date_of_edit=datetime.date.today(),
            is_active=True,
            client_group=[
                self.client_group
            ]
        )


class ClientTestCase(ClientBaseTestCase):

    def test_client_detail_get(self):
        url = reverse('client:client-detail', kwargs={'pk': self.client.pk})
        response = self.api_client.get(url)
        client = response.json()

        self.assertEqual(client['name'], self.client.name)
        self.assertEqual(client['other_names'], self.client.other_names)
        self.assertEqual(client['zip_code'], self.client.zip_code)
        self.assertEqual(client['email'], self.client.email)
        self.assertEqual(client['address'], self.client.address)
        self.assertEqual(client['region'], self.client.region)
        self.assertEqual(client['city'], self.client.city)
        self.assertEqual(client['website'], self.client.website)
        self.assertEqual(client['additional_info'],
                         self.client.additional_info)

        self.assertEqual(client['note'], self.client.note)
        self.assertEqual(client['employee_manager']['id'],
                         self.client.employee_manager.pk)

        self.assertEqual(client['client_status']['id'],
                         self.client.client_status.pk)

        self.assertEqual(client['employee_creator']['id'],
                         self.client.employee_creator.pk)

        self.assertEqual(client['date_of_create'],
                         self.client.date_of_create.strftime(DATE))

        self.assertEqual(client['date_of_edit'],
                         self.client.date_of_edit.strftime(DATE))
        self.assertTrue(client['is_active'])
        self.assertEqual(client['timezone'], self.client.timezone)

    def test_client_list_get(self):
        url = reverse('client:client-list')
        response = self.api_client.get(path=url)
        client = response.json()[0]

        self.assertEqual(client['name'], self.client.name)
        self.assertEqual(client['other_names'], self.client.other_names)
        self.assertEqual(client['zip_code'], self.client.zip_code)
        self.assertEqual(client['email'], self.client.email)
        self.assertEqual(client['address'], self.client.address)
        self.assertEqual(client['region'], self.client.region)
        self.assertEqual(client['city'], self.client.city)
        self.assertEqual(client['website'], self.client.website)
        self.assertEqual(client['additional_info'],
                         self.client.additional_info)

        self.assertEqual(client['note'], self.client.note)
        self.assertEqual(client['employee_manager']['id'],
                         self.client.employee_manager.id)

        self.assertEqual(client['client_status']['id'],
                         self.client.client_status.id)

        self.assertEqual(client['employee_creator']['id'],
                         self.client.employee_creator.id)

        self.assertEqual(client['date_of_create'],
                         self.client.date_of_create.strftime(DATE))

        self.assertEqual(client['date_of_edit'],
                         self.client.date_of_edit.strftime(DATE))

        self.assertEqual(client['timezone'], self.client.timezone)
        self.assertTrue(client['is_active'])

    def test_client_post(self):
        url = reverse('client:client-list')
        data = {
            'employee_manager_id': self.employee.pk,
            'employee_creator_id': self.employee.pk,
            'name': 'РАО «Харитонова»',
            'other_names': 'РАО Аристотель',
            'zip_code': '184682',
            'email': self.employee.email,
            'address': 'Россия, Ивановская область',
            'region': 'Ивановская область',
            'city': 'Иваново',
            'website': 'https://google.com',
            'timezone': datetime.datetime.now(tz=TZ),
            'additional_info': 'Компания занимается добычей угля',
            'note': 'Клиент также работает в странах СНГ',
            'client_status_id':  self.client_status.pk,
            'date_of_create': datetime.date.today(),
            'date_of_edit': datetime.date.today(),
            'is_active': True,
            'client_group_id': [
                self.client_group.pk
            ]
        }
        response = self.api_client.post(path=url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        client_id = response.json().get('id')

        self.assertTrue(Client.objects.filter(pk=client_id).exists())

        client = Client.objects.get(pk=client_id)

        self.assertEqual(client.employee_manager, self.employee)
        self.assertEqual(client.employee_creator, self.employee)
        self.assertEqual(client.name, data['name'])
        self.assertEqual(client.other_names, data['other_names'])
        self.assertEqual(client.zip_code, data['zip_code'])
        self.assertEqual(client.email, data['email'])
        self.assertEqual(client.address, data['address'])
        self.assertEqual(client.region, data['region'])
        self.assertEqual(client.city, data['city'])
        self.assertEqual(client.website, data['website'])
        self.assertEqual(client.timezone, data['timezone'])
        self.assertEqual(client.additional_info, data['additional_info'])
        self.assertEqual(client.note, data['note'])
        self.assertEqual(client.client_status_id, self.client_status.id)
        self.assertEqual(client.date_of_create, data['date_of_create'])
        self.assertEqual(client.date_of_edit, data['date_of_edit'])
        self.assertEqual(client.is_active, data['is_active'])
        self.assertEqual(client.client_group.instance.name, data['name'])


class ClientStatusTestCase(ClientBaseTestCase):

    def test_client_status_detail_get(self):
        url = reverse(
            'client:client_status-detail', kwargs={'pk': self.client_status.pk}
        )
        response = self.api_client.get(path=url)
        client_status = response.json()
        self.assertEqual(client_status['name'], self.client_status.name)

    def test_client_status_list_get(self):
        url = reverse('client:client_status-list')
        response = self.api_client.get(url)

        client_status = response.json()[0]

        self.assertEqual(client_status['name'], self.client_status.name)

    def test_client_status_post(self):
        url = reverse('client:client_status-list')
        data = {
            'name': 'Status'
        }
        response = self.api_client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        client_status_id = response.json().get('id')

        self.assertTrue(
            ClientStatus.objects.filter(pk=client_status_id).exists()
        )

        client_status = ClientStatus.objects.get(pk=client_status_id)

        self.assertEqual(client_status.name, data['name'])


class ClientGroupTestCase(ClientBaseTestCase):

    def test_client_group_detail_get(self):
        url = reverse(
            'client:client_group-detail', kwargs={'pk': self.client_group.pk}
        )
        response = self.api_client.get(path=url)
        client_group = response.json()

        self.assertEqual(client_group['name'], self.client_group.name)
        self.assertEqual(client_group['description'],
                         self.client_group.description)

        self.assertEqual(client_group['created_date'],
                         self.client_group.created_date.strftime(DATE))

        self.assertEqual(client_group['employee_creator'],
                         self.client_group.employee_creator.pk)

    def test_client_group_list_get(self):
        url = reverse('client:client_group-list')
        response = self.api_client.get(url)

        client_group = response.json()[0]

        self.assertEqual(client_group['name'], self.client_group.name)
        self.assertEqual(client_group['description'],
                         self.client_group.description)

        self.assertEqual(client_group['created_date'],
                         self.client_group.created_date.strftime(DATE))

        self.assertEqual(client_group['employee_creator'],
                         self.client_group.employee_creator.pk)

    def test_client_group_post(self):
        url = reverse('client:client_group-list')
        data = {
            'name': 'Group 0',
            'description': 'Description',
            'created_date': datetime.date.today(),
            'employee_creator_id': self.employee.pk
        }
        response = self.api_client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        client_group_id = response.json().get('id')

        self.assertTrue(
            ClientGroup.objects.filter(pk=client_group_id).exists()
        )

        client_group = ClientGroup.objects.get(pk=client_group_id)

        self.assertEqual(client_group.name, data['name'])
        self.assertEqual(client_group.description, data['description'])
        self.assertEqual(client_group.created_date, data['created_date'])
        self.assertEqual(client_group.employee_creator_id,
                         data['employee_creator_id'])
