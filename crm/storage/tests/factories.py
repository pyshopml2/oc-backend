import factory
from storage.models import Storage

class StorageFactory(factory.DjangoModelFactory):

	class Meta:
		model = Storage

	name = factory.Faker('text', max_nb_chars=20)
	address = factory.Faker('text', max_nb_chars=20)
	mode = factory.Faker('text', max_nb_chars=20)
	first_name = factory.Faker('first_name')
	middle_name = factory.Faker('first_name')
	last_name = factory.Faker('last_name')
	phone_number = '9633609225'
	scheme = factory.Faker('file_name')
	note = factory.Faker('text')


