from django.db import models
from user.models import User

# Модель сотрудника
class Employee(User):
    login_skype = models.CharField(max_length=50, blank=True, verbose_name='Skype')
    confirmed_email = models.BooleanField(default=False, verbose_name='Подтвержденный email')
    employee_group = models.ForeignKey('GroupEmployee', related_name='employee_group',
                                 on_delete=models.PROTECT, default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

# Модель группы сотрудников
class GroupEmployee(models.Model):
    name = models.CharField(max_length=60, verbose_name='Имя группы')
    description = models.CharField(max_length=400, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    creator = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'