import datetime

from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .factories import *
from core.tests.consts import *
from position.tests.factories import PositionFactory

fake = Faker()


class EmployeeBaseTestCase(APITestCase):

    def setUp(self):
        self.position = PositionFactory()
        self.group = EmployeeGroupFactory(
            name='Name',
            description='This is description for this group',
            creation_date=datetime.datetime.now(tz=TZ),
            creator=None
        )
        self.employee = EmployeeFactory(
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
            login_skype='trelop',
            confirmed_email=True,
            group=self.group
        )


class EmployeeTestCase(EmployeeBaseTestCase):

    def test_employee_detail_get(self):
        url = reverse(
            'employee:employee-detail', kwargs={'pk': self.employee.pk})

        response = self.client.get(path=url)
        employee = response.json()

        self.assertEqual(employee['first_name'],
                         self.employee.first_name)

        self.assertEqual(employee['middle_name'],
                         self.employee.middle_name)

        self.assertEqual(employee['last_name'],
                         self.employee.last_name)

        self.assertEqual(employee['email'], self.employee.email)

        self.assertEqual(employee['user_position']['id'],
                         self.employee.user_position.pk)

        self.assertEqual(employee['date_of_birth'],
                         self.employee.date_of_birth.strftime(DATE))

        self.assertEqual(employee['phone_number'],
                         self.employee.phone_number)

        self.assertEqual(employee['extra_phone_number'],
                         self.employee.extra_phone_number)

        self.assertEqual(employee['other_contacts'],
                         self.employee.other_contacts)

        self.assertEqual(employee['timezone'],
                         self.employee.timezone)

        self.assertEqual(employee['status'],
                         self.employee.status)

        self.assertEqual(employee['login_skype'],
                         self.employee.login_skype)

        self.assertEqual(employee['confirmed_email'],
                         self.employee.confirmed_email)

        self.assertEqual(employee['group']['id'],
                         self.employee.group.pk)

        self.assertTrue(employee['is_active'])
        self.assertTrue(employee['is_staff'])
        self.assertFalse(employee['is_superuser'])

    def test_employee_list_get(self):
        url = reverse('employee:employee-list')
        response = self.client.get(path=url)
        employee = response.json()[0]

        self.assertEqual(employee['first_name'],
                         self.employee.first_name)

        self.assertEqual(employee['middle_name'],
                         self.employee.middle_name)

        self.assertEqual(employee['last_name'],
                         self.employee.last_name)

        self.assertEqual(employee['email'], self.employee.email)
        self.assertEqual(employee['user_position']['id'],
                         self.employee.user_position.pk)

        self.assertEqual(employee['date_of_birth'],
                         self.employee.date_of_birth.strftime(DATE))

        self.assertEqual(employee['phone_number'],
                         self.employee.phone_number)

        self.assertEqual(employee['extra_phone_number'],
                         self.employee.extra_phone_number)

        self.assertEqual(employee['other_contacts'],
                         self.employee.other_contacts)

        self.assertEqual(employee['timezone'],
                         self.employee.timezone)

        self.assertEqual(employee['status'],
                         self.employee.status)

        self.assertEqual(employee['login_skype'],
                         self.employee.login_skype)

        self.assertEqual(employee['confirmed_email'],
                         self.employee.confirmed_email)

        self.assertEqual(employee['group']['id'],
                         self.employee.group.pk)

        self.assertTrue(employee['is_active'])
        self.assertTrue(employee['is_staff'])
        self.assertFalse(employee['is_superuser'])

    def test_employee_post(self):
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
            'login_skype': 'trelop',
            'confirmed_email': True,
            'group_id': self.group.pk,
            'password': 'password'
        }
        url = reverse('employee:employee-list')
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)

        employee_id = response.json().get('id')

        self.assertTrue(Employee.objects.filter(pk=employee_id).exists())

        employee = Employee.objects.get(pk=employee_id)

        self.assertEqual(employee.first_name, data['first_name'])
        self.assertEqual(employee.middle_name, data['middle_name'])
        self.assertEqual(employee.last_name, data['last_name'])
        self.assertEqual(employee.email, data['email'])
        self.assertEqual(employee.group_id, data['group_id'])
        self.assertEqual(employee.date_of_birth, data['date_of_birth'])
        self.assertEqual(employee.phone_number,
                         data['phone_number'])

        self.assertEqual(employee.extra_phone_number,
                         data['extra_phone_number'])

        self.assertEqual(employee.other_contacts,
                         data['other_contacts'])

        self.assertEqual(employee.timezone, data['timezone'])
        self.assertTrue(employee.is_active)
        self.assertTrue(employee.is_staff)
        self.assertFalse(employee.is_superuser)
        self.assertEqual(employee.status, data['status'])
        self.assertEqual(employee.login_skype, data['login_skype'])
        self.assertEqual(employee.confirmed_email, data['confirmed_email'])
        self.assertEqual(employee.group.pk, data['group_id'])


class EmployeeGroupTestCase(EmployeeBaseTestCase):

    def test_employee_group_detail_get(self):
        url = reverse(
            'employee:employee_group-detail', kwargs={'pk': self.group.pk})
        response = self.client.get(path=url)
        group = response.json()

        self.assertEqual(group['name'], self.group.name)
        self.assertEqual(group['description'], self.group.description)

    def test_employee_group_list_get(self):
        url = reverse('employee:employee_group-list')
        response = self.client.get(path=url)
        group = response.json()[0]

        self.assertEqual(group['name'], self.group.name)
        self.assertEqual(group['description'], self.group.description)

    def test_employee_group_post(self):
        data = {
            'name': 'Группа клиентов',
            'description': 'Описание данной группы',
            'creation_date': '2018-08-29T20:43:18.869351+03:00',
            'creator_id': self.employee.pk
        }
        url = reverse('employee:employee_group-list')
        response = self.client.post(url, data)
        employee_group_id = response.json().get('id')

        self.assertTrue(
            EmployeeGroup.objects.filter(pk=employee_group_id).exists())

        employee_group = EmployeeGroup.objects.get(pk=employee_group_id)
        self.assertEqual(employee_group.name, data['name'])
        self.assertEqual(employee_group.description, data['description'])
        self.assertEqual(employee_group.creator_id, data['creator_id'])
