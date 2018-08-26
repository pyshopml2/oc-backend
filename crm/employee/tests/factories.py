import factory.fuzzy
import factory
import pytz
from employee.models import *
from user.models import STATUS as user_status

from user.tests.factories import *
from position.tests.factories import PositionFactory

STATUS_USER = [x[0] for x in user_status]

class EmployeeFactory(factory.DjangoModelFactory):

	first_name = factory.Faker('first_name')
	middle_name = factory.Faker('first_name')
	last_name = factory.Faker('last_name')
	email = factory.Faker('company_email')
	user_position = factory.SubFactory(PositionFactory)
	date_of_birth = factory.Faker('past_date')
	phone_number = 9633609226
	extra_phone_number = 9633609226
	other_contacts = factory.Faker('text', max_nb_chars=49)
	timezone = factory.Faker('iso8601', tzinfo=pytz.utc)
	is_active = True
	is_staff = True
	is_superuser = False
	status = factory.fuzzy.FuzzyChoice(STATUS_USER)
	login_skype = factory.Faker('user_name')
	confirmed_email = True
	password = factory.Faker('password')
	#group = factory.SubFactory('employee.tests.factories.EmployeeGroupFactory')

	class Meta:
		model = Employee

class BuildEmployeeFactory(EmployeeFactory):

	class Meta:
		strategy = factory.STUB_STRATEGY

class EmployeeGroupFactory(factory.Factory):

	class Meta:
		model = EmployeeGroup

	name = factory.Faker('text', max_nb_chars=20)
	description = factory.Faker('text', max_nb_chars=49)
	created_at = factory.Faker('iso8601')
	creator = factory.SubFactory(EmployeeFactory)