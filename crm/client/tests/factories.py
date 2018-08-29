import pytz
import factory

from client.models import *
from employee.tests.factories import EmployeeFactory

class ClientStatusFactory(factory.DjangoModelFactory):

	class Meta:
		model = ClientStatus

	name = factory.Faker('sentence', nb_words=4)


class ClientGroupFactory(factory.DjangoModelFactory):

	class Meta:
		model = ClientGroup

	name = factory.Sequence(lambda n: "Group {0}".format(n))
	description = factory.Faker('sentence', nb_words=4)
	created_date = factory.Faker('iso8601')
	employee_creator = factory.SubFactory(EmployeeFactory)

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
	timezone = factory.Faker('iso8601', tzinfo=pytz.utc)
	additional_info = factory.Faker('sentence', nb_words=4)
	note = factory.Faker('sentence', nb_words=4)
	employee_manager = factory.SubFactory(EmployeeFactory)
	client_status = factory.SubFactory(ClientStatusFactory)
	employee_creator = factory.SubFactory(EmployeeFactory)
	date_of_create = factory.Faker('past_date')
	date_of_edit = factory.Faker('date')
	is_active = True
	client_group = factory.SubFactory(ClientGroupFactory)

	@factory.post_generation
	def client_group(self, create, extracted):
		if not create:
			return

		if extracted:
			for group in extracted:
				self.client_group.add(group)
