from django.db import models
from employee.models import Employee
from person.models import ContactPerson

class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование задачи')
    datetime_of_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_todo = models.DateField(verbose_name='Дата выполнения')
    time_todo = models.TimeField(verbose_name='Время выполнения')
    #contact_person = models.ForeignKey(ContactPerson)
    status = models.CharField(max_length=20, verbose_name='Статус')
    priority = models.CharField(max_length=20, verbose_name='Приоритет')
    task_description = models.TextField(verbose_name='Описание задачи', blank=True)
    task_creator = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='task_creator',
                                     blank=True, null=True, verbose_name='Создатель')
    task_executor = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='task_executor',
                                      blank=True, null=True, verbose_name='Исполнитель')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
