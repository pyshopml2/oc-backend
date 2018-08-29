import pytz

import factory.fuzzy
import factory

from task.models import Task
from task.models import STATUS as task_status
from task.models import PRIORITY as task_prioity
from employee.tests.factories import EmployeeFactory

PRIORITY_TASK = [x[0] for x in task_prioity]
STATUS_TASK = [x[0] for x in task_status]


class TaskFactory(factory.DjangoModelFactory):

	class Meta:
		model = Task

	name = factory.Faker('sentence', nb_words=4)
	datetime_of_create = factory.Faker('date_time_this_month', tzinfo=pytz.UTC)
	date_time_todo = factory.Faker('future_datetime', tzinfo=pytz.UTC)
	status = factory.fuzzy.FuzzyChoice(STATUS_TASK)
	priority = factory.fuzzy.FuzzyChoice(PRIORITY_TASK)
	task_description = factory.Faker('sentence', nb_words=4)
	task_creator = factory.SubFactory(EmployeeFactory)
	task_executor = factory.SubFactory(EmployeeFactory)