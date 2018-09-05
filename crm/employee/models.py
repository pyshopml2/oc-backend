from django.db import models
from user.models import User


class Employee(User):
    login_skype = models.CharField(
        max_length=50, blank=True, verbose_name='Skype')

    confirmed_email = models.BooleanField(
        default=False, verbose_name='Подтвержденный email')

    group = models.ForeignKey(
        'EmployeeGroup', related_name='employee_group',
        on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return super(Employee, self).__str__()


class EmployeeGroup(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя группы')
    description = models.CharField(max_length=300, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата создания')
    creator = models.ForeignKey(
        Employee, related_name='employee_group',
        on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
