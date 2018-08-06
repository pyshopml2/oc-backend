from django.db import models
from employee.models import Employee

class Task(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование задачи')
    datetime_of_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_todo = models.DateField(verbose_name='Дата выполнения')
    time_todo = models.TimeField(verbose_name='Время выполнения')
    status = models.CharField(max_length=20, verbose_name='Статус')
    priority = models.CharField(max_length=20, verbose_name='Приоритет')
    text = models.TextField(verbose_name='Описание задачи')
    creator = models.OneToOneField(Employee, on_delete=models.PROTECT, verbose_name='Создатель')
    executor = models.OneToOneField(Employee, on_delete=models.PROTECT, verbose_name='Создатель')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'