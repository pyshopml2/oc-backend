import factory
from position.models import Position


class PositionFactory(factory.DjangoModelFactory):

    class Meta:
        model = Position

    name = factory.Faker('job')
    description = factory.Faker('sentence', nb_words=4)
