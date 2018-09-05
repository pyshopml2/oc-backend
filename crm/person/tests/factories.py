import pytz

import factory
import factory.fuzzy

from person.models import *
from user.tests.factories import *
from user.models import STATUS as user_status
from client.tests.factories import ClientFactory

STATUS_USER = [x[0] for x in user_status]


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
    other_contacts = factory.Faker('sentence', nb_words=4)
    timezone = factory.Faker('iso8601', tzinfo=pytz.utc)
    is_active = True
    is_staff = True
    is_superuser = False
    status = factory.fuzzy.FuzzyChoice(STATUS_USER)
    region = factory.Faker('address')
    city = factory.Faker('city')
    dialing_code = 34
    client = factory.SubFactory(ClientFactory)
