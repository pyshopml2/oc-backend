from django.db import models
from employee.models import Employee
from person.models import ContactPerson

PRIORITY = (
    ('1', 'Высокий'),
    ('2', 'Обычный'),
    ('3', 'Низкий'),
)

STATUS = (
    ('1', 'Выполняется'),
    ('2', 'Выполнена'),
    ('3', 'Перенесена'),
    ('4', 'Отменена'),
    ('5', 'Не выполнена'),
)


class Task(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Наименование задачи',
        help_text='Наименование задачи')
    datetime_of_create = models.DateTimeField(
        verbose_name='Дата и время начала',
        help_text='Дата и время начала')

    date_time_todo = models.DateTimeField(
        verbose_name='Дата и время окончания',
        help_text='Дата и время окончания')

    # contact_person = models.ForeignKey(ContactPerson)
    status = models.CharField(
        max_length=1, choices=STATUS, verbose_name='Статус',
        help_text='Статус задачи')

    priority = models.CharField(
        max_length=1, choices=PRIORITY, verbose_name='Приоритет',
        help_text='Приоритет')

    task_description = models.TextField(
        verbose_name='Описание задачи', blank=True,
        help_text='Описание задачи')

    task_creator = models.ForeignKey(
        Employee, on_delete=models.PROTECT,
        related_name='task_creator', blank=True,
        null=True, verbose_name='Постановщик задачи',
        help_text='Постановщик задачи')

    task_executor = models.ForeignKey(
        Employee, on_delete=models.PROTECT,
        related_name='task_executor', blank=True,
        null=True, verbose_name='Исполнитель задачи',
        help_text='Исполнитель задачи')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name
