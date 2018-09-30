import pytz

import factory.fuzzy
import factory

from task import models
from employee.tests.factories import EmployeeFactory

PRIORITY_TASK = [x[0] for x in models.PRIORITY]
STATUS_TASK = [x[0] for x in models.STATUS]


class TaskFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Task

    name = factory.Faker('sentence', nb_words=4)
    creation_date = factory.Faker(
        'date_time_this_month', tzinfo=pytz.UTC)
    expiration_date = factory.Faker('future_datetime', tzinfo=pytz.UTC)
    status = factory.fuzzy.FuzzyChoice(STATUS_TASK)
    priority = factory.fuzzy.FuzzyChoice(PRIORITY_TASK)
    task_description = factory.Faker('sentence', nb_words=4)
    task_creator = factory.SubFactory(EmployeeFactory)
    task_executor = factory.SubFactory(EmployeeFactory)
