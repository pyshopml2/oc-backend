import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
django.setup()

import pytz

import factory.fuzzy
import factory

from client import models as c_models
from document import models as d_models
from employee import models as e_models
from person import models as p_models
from position import models as pos_models
from storage import models as s_models
from task import models as t_models

from document.models import STATUS as document_status
from user.models import STATUS as user_status
from task.models import PRIORITY as task_prioity
from task.models import STATUS as task_status


class PositionFactory(factory.DjangoModelFactory):

    class Meta:
        model = pos_models.Position

    name = factory.Faker('job')
    description = factory.Faker('text')


class EmployeeGroupFactory(factory.DjangoModelFactory):

    class Meta:
        model = e_models.EmployeeGroup

    name = factory.Sequence(lambda n: "Group {}".format(n))
    description = factory.Faker('text')
    creation_date = factory.Faker('iso8601')
    # creator


class ClientStatusFactory(factory.DjangoModelFactory):

    class Meta:
        model = c_models.ClientStatus

    name = factory.Faker('text', max_nb_chars=20)


class CatalogDocumentsFactory(factory.DjangoModelFactory):

    class Meta:
        model = d_models.CatalogDocuments

    name = factory.Faker('text', max_nb_chars=20)
    description = factory.Faker('text', max_nb_chars=200)


class StorageFactory(factory.DjangoModelFactory):

    class Meta:
        model = s_models.Storage

    name = factory.Faker('text', max_nb_chars=20)
    address = factory.Faker('text', max_nb_chars=20)
    mode = factory.Faker('text', max_nb_chars=20)
    first_name = factory.Faker('first_name')
    middle_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    phone_number = 9633609226
    scheme = factory.Faker('file_name')
    note = factory.Faker('text')


StorageFactory()


# **

STATUS_DOCUMENT = [x[0] for x in document_status]


class DocumentFactory(factory.DjangoModelFactory):

    class Meta:
        model = d_models.Document

    catalog_documents = factory.SubFactory(CatalogDocumentsFactory)
    status = factory.fuzzy.FuzzyChoice(STATUS_DOCUMENT)
    created_date = factory.Faker('iso8601')


DocumentFactory()

STATUS_USER = [x[0] for x in user_status]


class EmployeeFactory(factory.DjangoModelFactory):

    class Meta:
        model = e_models.Employee

    first_name = factory.Faker('first_name')
    middle_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('company_email')
    user_position = factory.SubFactory(PositionFactory)
    date_of_birth = factory.Faker('past_date')
    phone_number = 9633609226
    extra_phone_number = 9633609226
    other_contacts = factory.Faker('text')
    timezone = factory.Faker('iso8601', tzinfo=pytz.utc)
    is_active = True
    is_staff = True
    is_superuser = False
    status = factory.fuzzy.FuzzyChoice(STATUS_USER)
    login_skype = factory.Faker('user_name')
    confirmed_email = True
    group = factory.SubFactory(EmployeeGroupFactory)


class ClientGroupFactory(factory.DjangoModelFactory):

    class Meta:
        model = c_models.ClientGroup

    name = factory.Sequence(lambda n: "Group {0}".format(n))
    description = factory.Faker('text')
    created_date = factory.Faker('iso8601')
    employee_creator = factory.SubFactory(EmployeeFactory)


ClientGroupFactory()


class ClientFactory(factory.DjangoModelFactory):

    class Meta:
        model = c_models.Client

    name = factory.Faker('company')
    other_names = factory.Faker('company')
    zip_code = factory.Faker('postcode')
    email = factory.Faker('company_email')
    address = factory.Faker('address')
    region = factory.Faker('address')
    city = factory.Faker('city')
    website = 'https://google.com'
    group_client = factory.SubFactory(ClientGroupFactory)
    timezone = factory.Faker('iso8601', tzinfo=pytz.utc)
    additional_info = factory.Faker('text')
    note = factory.Faker('text')
    employee_manager = factory.SubFactory(EmployeeFactory)
    client_status = factory.SubFactory(ClientStatusFactory)
    employee_creator = factory.SubFactory(EmployeeFactory)
    creation_date = factory.Faker('past_date')
    date_last_editing = factory.Faker('date')
    is_active = True

    @factory.post_generation
    def group_client(self, create, extracted):
        if not create:
            return

        if extracted:
            for group in extracted:
                self.group_client.add(group)


class PersonFactory(factory.DjangoModelFactory):

    class Meta:
        model = p_models.ContactPerson

    first_name = factory.Faker('first_name')
    middle_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('company_email')
    user_position = factory.SubFactory(PositionFactory)
    date_of_birth = factory.Faker('past_date')
    phone_number = 9633609226
    extra_phone_number = 9633609226
    other_contacts = factory.Faker('text')
    timezone = factory.Faker('iso8601', tzinfo=pytz.utc)
    is_active = True
    is_staff = True
    is_superuser = False
    status = factory.fuzzy.FuzzyChoice(STATUS_USER)
    region = factory.Faker('address')
    city = factory.Faker('city')
    dialing_code = 34
    client = factory.SubFactory(ClientFactory)


PersonFactory()

PRIORITY_TASK = [x[0] for x in task_prioity]
STATUS_TASK = [x[0] for x in task_status]


class TaskFactory(factory.DjangoModelFactory):

    class Meta:
        model = t_models.Task

    name = factory.Faker('text')
    creation_date = factory.Faker('date_time_this_month', tzinfo=pytz.UTC)
    expiration_date = factory.Faker('future_datetime', tzinfo=pytz.UTC)
    status = factory.fuzzy.FuzzyChoice(STATUS_TASK)
    priority = factory.fuzzy.FuzzyChoice(PRIORITY_TASK)
    task_description = factory.Faker('text')
    task_creator = factory.SubFactory(EmployeeFactory)
    task_executor = factory.SubFactory(EmployeeFactory)


TaskFactory()
