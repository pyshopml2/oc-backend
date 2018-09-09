import datetime

from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import *
from core.tests.consts import *
from client.tests.factories import ClientFactory
from position.tests.factories import PositionFactory

fake = Faker()


class PersonBaseTestCase(APITestCase):

    def setUp(self):
        self.position = PositionFactory()
        self.company = ClientFactory(
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
            employee_manager=None,
            client_status=None,
            employee_creator=None,
            creation_date=datetime.date.today(),
            date_last_editing=datetime.date.today(),
            is_active=True,
            client_group=[]
        )
        self.person = PersonFactory(
            first_name='Александр',
            middle_name='Сергеевич',
            last_name='Зубов',
            email='trelop@gmail.com',
            user_position=self.position,
            date_of_birth=datetime.datetime.today(),
            phone_number='9633609225',
            extra_phone_number='9633609225',
            other_contacts='Telegram - trelop',
            timezone='2018-08-29T20:43:18.869351+03:00',
            is_active=True,
            is_staff=True,
            is_superuser=False,
            status='1',
            region='Мурманская область',
            city='Мурманск',
            dialing_code='8152',
            client=self.company
        )


class PersonTestCase(PersonBaseTestCase):

    def test_person_detail_get(self):
        url = reverse('person:person-detail', kwargs={'pk': self.person.pk})
        response = self.client.get(path=url)
        person = response.json()

        self.assertEqual(person['first_name'], self.person.first_name)
        self.assertEqual(person['middle_name'], self.person.middle_name)
        self.assertEqual(person['last_name'], self.person.last_name)
        self.assertEqual(person['email'], self.person.email)
        self.assertEqual(person['user_position'], self.person.user_position.pk)
        self.assertEqual(person['date_of_birth'],
                         self.person.date_of_birth.strftime(DATE))
        self.assertEqual(person['phone_number'], self.person.phone_number)
        self.assertEqual(person['extra_phone_number'],
                         self.person.extra_phone_number)
        self.assertEqual(person['other_contacts'], self.person.other_contacts)
        self.assertEqual(person['timezone'], self.person.timezone)
        self.assertTrue(person['is_active'])
        self.assertTrue(person['is_staff'])
        self.assertFalse(person['is_superuser'])
        self.assertEqual(person['status'], self.person.status)
        self.assertEqual(person['region'], self.person.region)
        self.assertEqual(person['city'], self.person.city)
        self.assertEqual(person['dialing_code'], self.person.dialing_code)
        self.assertEqual(person['client'], self.person.client.pk)

    def test_person_list_get(self):
        url = reverse('person:person-list')
        response = self.client.get(path=url)
        person = response.json()[0]

        self.assertEqual(person['first_name'], self.person.first_name)
        self.assertEqual(person['middle_name'], self.person.middle_name)
        self.assertEqual(person['last_name'], self.person.last_name)
        self.assertEqual(person['email'], self.person.email)
        self.assertEqual(person['user_position'], self.person.user_position.pk)
        self.assertEqual(person['date_of_birth'],
                         self.person.date_of_birth.strftime(DATE))
        self.assertEqual(person['phone_number'], self.person.phone_number)
        self.assertEqual(person['extra_phone_number'],
                         self.person.extra_phone_number)
        self.assertEqual(person['other_contacts'], self.person.other_contacts)
        self.assertEqual(person['timezone'], self.person.timezone)
        self.assertTrue(person['is_active'])
        self.assertTrue(person['is_staff'])
        self.assertFalse(person['is_superuser'])
        self.assertEqual(person['status'], self.person.status)
        self.assertEqual(person['region'], self.person.region)
        self.assertEqual(person['city'], self.person.city)
        self.assertEqual(person['dialing_code'], self.person.dialing_code)
        self.assertEqual(person['client'], self.person.client.pk)

    def test_person_post(self):
        email = fake.email()
        data = {
            'first_name': 'Александр',
            'middle_name': 'Сергеевич',
            'last_name': 'Зубов',
            'email': email,
            'user_position_id': self.position.pk,
            'date_of_birth': datetime.date.today(),
            'phone_number': '9633609225',
            'extra_phone_number': '9633609225',
            'other_contacts': 'Telegram - trelop',
            'timezone': datetime.datetime.now(tz=TZ),
            'is_active': True,
            'is_staff': True,
            'is_superuser': False,
            'status': '1',
            'region': 'Мурманская область',
            'city': 'Мурманск',
            'dialing_code': '8152',
            'company_id': self.company.pk,
            'password': 'password'

        }
        url = reverse('person:person-list')
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        person_id = response.json().get('id')

        self.assertTrue(ContactPerson.objects.filter(pk=person_id).exists())

        person = ContactPerson.objects.get(pk=person_id)

        self.assertEqual(person.first_name, data['first_name'])
        self.assertEqual(person.middle_name, data['middle_name'])
        self.assertEqual(person.last_name, data['last_name'])
        self.assertEqual(person.email, data['email'])
        self.assertEqual(person.date_of_birth, data['date_of_birth'])
        self.assertEqual(person.phone_number, data['phone_number'])
        self.assertEqual(person.extra_phone_number, data['extra_phone_number'])
        self.assertEqual(person.other_contacts, data['other_contacts'])
        self.assertEqual(person.timezone, data['timezone'])
        self.assertTrue(person.is_active)
        self.assertTrue(person.is_staff)
        self.assertFalse(person.is_superuser)
        self.assertEqual(person.status, data['status'])
        self.assertEqual(person.region, data['region'])
        self.assertEqual(person.city, data['city'])
        self.assertEqual(person.dialing_code, data['dialing_code'])
        self.assertEqual(person.client.pk, data['company_id'])
