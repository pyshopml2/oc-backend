import datetime

from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.tests.consts import *
from client.tests.factories import ClientFactory
from task.tests.factories import TaskFactory
from employee.tests.factories import EmployeeFactory, EmployeeGroupFactory
from position.tests.factories import PositionFactory

from rest_framework_simplejwt.tokens import AccessToken

fake = Faker()


class PersonBaseTestCase(APITestCase):

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
            employee_manager=self.employee,
            client_status=None,
            employee_creator=None,
            creation_date=datetime.date.today(),
            date_last_editing=datetime.date.today(),
            is_active=True,
            client_group=[]
        )
        self.task = TaskFactory(
            name='Task',
            creation_date='2018-08-29T20:43:18.869351+03:00',
            expiration_date='2018-08-29T20:43:18.869351+03:00',
            status='1',
            priority='1',
            task_description='Description',
            task_creator=self.employee,
            task_executor=self.employee
        )



class AccountTestCase(PersonBaseTestCase):

    def test_account_detail_get(self):
        url = reverse('account')
        access_token = AccessToken.for_user(self.employee)
        auth_headers = {
            'HTTP_AUTHORIZATION': 'Bearer {}'.format(access_token),
        }
        response = self.client.get(path=url, **auth_headers)
        account = response.json()
        self.assertEqual(account['clients'][0]['name'],
                         self.company.name)
        self.assertEqual(account['clients'][0]['other_names'],
                         self.company.other_names)
        self.assertEqual(account['clients'][0]['zip_code'],
                         self.company.zip_code)
        self.assertEqual(account['clients'][0]['email'],
                         self.company.email)
        self.assertEqual(account['clients'][0]['address'],
                         self.company.address)
        self.assertEqual(account['clients'][0]['region'],
                         self.company.region)
        self.assertEqual(account['clients'][0]['city'],
                         self.company.city)
        self.assertEqual(account['clients'][0]['website'],
                         self.company.website)
        self.assertEqual(account['clients'][0]['timezone'],
                         '2018-08-29T20:43:18.869351+03:00')
        self.assertEqual(account['clients'][0]['additional_info'],
                         self.company.additional_info)
        self.assertEqual(account['clients'][0]['note'],
                         self.company.note)
        self.assertEqual(account['clients'][0]['creation_date'],
                         datetime.date.today().strftime(DATE))
        self.assertEqual(account['clients'][0]['date_last_editing'],
                         datetime.date.today().strftime(DATE))
        self.assertEqual(account['clients'][0]['date_last_editing'],
                         datetime.date.today().strftime(DATE))
        self.assertEqual(account['clients'][0]['is_active'],
                         self.company.is_active)
        self.assertEqual(account['clients'][0]['client_status'],
                         self.company.client_status)
        self.assertEqual(account['clients'][0]['employee_creator'],
                         self.company.employee_creator)
        self.assertEqual(account['clients'][0]['client_group'], [])
        self.assertEqual(account['clients'][0]['employee_manager']['id'],
                         self.company.employee_manager.pk)

        self.assertEqual(account['employees'][0]['first_name'],
                         self.employee.first_name)
        self.assertEqual(account['employees'][0]['middle_name'],
                         self.employee.middle_name)
        self.assertEqual(account['employees'][0]['last_name'],
                         self.employee.last_name)
        self.assertEqual(account['employees'][0]['email'], self.employee.email)
        self.assertEqual(account['employees'][0]['user_position']['id'],
                         self.employee.user_position.pk)
        self.assertEqual(account['employees'][0]['date_of_birth'],
                         self.employee.date_of_birth.strftime(DATE))
        self.assertEqual(account['employees'][0]['phone_number'],
                         self.employee.phone_number)
        self.assertEqual(account['employees'][0]['extra_phone_number'],
                         self.employee.extra_phone_number)
        self.assertEqual(account['employees'][0]['other_contacts'],
                         self.employee.other_contacts)
        self.assertEqual(account['employees'][0]['timezone'],
                         self.employee.timezone)
        self.assertEqual(account['employees'][0]['status'],
                         self.employee.status)
        self.assertEqual(account['employees'][0]['login_skype'],
                         self.employee.login_skype)
        self.assertEqual(account['employees'][0]['confirmed_email'],
                         self.employee.confirmed_email)
        self.assertEqual(account['employees'][0]['group']['id'],
                         self.employee.group.pk)
        self.assertTrue(account['employees'][0]['is_active'])
        self.assertTrue(account['employees'][0]['is_staff'])
        self.assertFalse(account['employees'][0]['is_superuser'])

        self.assertEqual(account['tasks'][0]['name'], self.task.name)
        self.assertEqual(account['tasks'][0]['creation_date'],
                         self.task.creation_date)

        self.assertEqual(account['tasks'][0]['expiration_date'], self.task.expiration_date)
        self.assertEqual(account['tasks'][0]['status'], self.task.status)
        self.assertEqual(account['tasks'][0]['priority'], self.task.priority)
        self.assertEqual(account['tasks'][0]['task_description'], self.task.task_description)
        self.assertEqual(account['tasks'][0]['task_creator']['id'], self.task.task_creator.pk)
        self.assertEqual(account['tasks'][0]['task_executor']['id'],
                         self.task.task_executor.pk)