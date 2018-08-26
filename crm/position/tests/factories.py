import factory

from position.models import *

class PositionFactory(factory.DjangoModelFactory):

	class Meta:
		model = Position

	name = factory.Faker('job')
	description = factory.Faker('text', max_nb_chars=49)