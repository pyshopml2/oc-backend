import factory
from storage.models import Storage

class StorageFactory(factory.DjangoModelFactory):

	class Meta:
		model = Storage

	name = factory.Faker('sentence', nb_words=4)
	address = factory.Faker('sentence', nb_words=4)
	mode = factory.Faker('sentence', nb_words=4)
	first_name = factory.Faker('first_name')
	middle_name = factory.Faker('first_name')
	last_name = factory.Faker('last_name')
	phone_number = '9633609225'
	scheme = factory.Faker('file_name', category='image', extension='png')
	note = factory.Faker('sentence', nb_words=4)


