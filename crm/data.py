import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm.settings')
django.setup()

import factory.fuzzy
import factory
from client.models import *
from document.models import *
from employee.models import *
from person.models import *
from position.models import *
from storage.models import *
from task.models import *

from user.models import STATUS as user_status

# *

class PositionFactory(factory.DjangoModelFactory):

	class Meta:
		model = Position

	name = factory.Faker('job')
	description = factory.Faker('text')

class GroupEmployeeFactory(factory.DjangoModelFactory):

	class Meta:
		model = GroupEmployee

	name = factory.Sequence(lambda n: "Group #%s" % n)
	description = factory.Faker('text')
	created_at = factory.Faker('iso8601')
	#creator

class ClientStatusFactory(factory.DjangoModelFactory):

	class Meta:
		model = ClientStatus

	name = 'active'

# **

STATUS_USER = [x[0] for x in user_status]

class EmployeeFactory(factory.DjangoModelFactory):

	class Meta:
		model = Employee

	first_name = factory.Faker('first_name')
	middle_name = factory.Faker('first_name')
	last_name = factory.Faker('last_name')
	email = factory.Faker('company_email')
	user_position = factory.SubFactory(PositionFactory)
	date_of_birth = factory.Faker('past_date')
	phone_number = 9633609226
	extra_phone_number = 9633609226
	other_contacts = factory.Faker('text')
	#timezone = factory.Faker('timezone')
	is_active = True
	is_staff = True
	is_superuser = False
	status = factory.fuzzy.FuzzyChoice(STATUS_USER)
	login_skype = factory.Faker('user_name')
	confirmed_email = True
	employee_group = factory.SubFactory(GroupEmployeeFactory)

class GroupClientFactory(factory.DjangoModelFactory):

	class Meta:
		model = GroupClient

	name = factory.Sequence(lambda n: "Group #%s" % n)
	description = factory.Faker('text')
	created_date = factory.Faker('iso8601')
	cmployee_creator = factory.SubFactory(EmployeeFactory)

GroupClientFactory()

class ClientFactory(factory.DjangoModelFactory):

	class Meta:
		model = Client

	name = factory.Faker('company')
	other_names = factory.Faker('company')
	zip_code = factory.Faker('postcode')
	email = factory.Faker('company_email')
	address = factory.Faker('address')
	region = factory.Faker('address')
	city = factory.Faker('city')
	website = 'https://google.com'
	group_client = factory.SubFactory(GroupClientFactory)
	#timezone = ''
	additional_info = factory.Faker('text')
	note = factory.Faker('text')
	employee_manager = factory.SubFactory(EmployeeFactory)
	client_status = factory.SubFactory(ClientStatusFactory)
	employee_creator = factory.SubFactory(EmployeeFactory)
	#date_of_create
	#date_of_edit
	is_active = True

	@factory.post_generation
	def group_client(self, create, extracted, **kwargs):
		if not create:
			# Simple build, do nothing.
			return

		if extracted:
			# A list of groups were passed in, use them
			for group in extracted:
				self.group_client.add(group)

class PersonFactory(factory.DjangoModelFactory):

	class Meta:
		model = ContactPerson

	first_name = factory.Faker('first_name')
	middle_name = factory.Faker('first_name')
	last_name = factory.Faker('last_name')
	email = factory.Faker('company_email')
	user_position = factory.SubFactory(PositionFactory)
	date_of_birth = factory.Faker('past_date')
	phone_number = 9633609226
	extra_phone_number = 9633609226
	other_contacts = factory.Faker('text')
	# timezone
	is_active = True
	is_staff = True
	is_superuser = False
	status = factory.fuzzy.FuzzyChoice(STATUS_USER)
	region = factory.Faker('address')
	city = factory.Faker('city')
	dialing_code = 34
	client = factory.SubFactory(ClientFactory)

PersonFactory()