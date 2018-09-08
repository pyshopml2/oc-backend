from django.db import models
from user.models import User


class Employee(User):
    login_skype = models.CharField(
        max_length=50, blank=True, verbose_name='Skype',
        help_text='Skype')

    confirmed_email = models.BooleanField(
        default=False, verbose_name='Подтвержденный email',
        help_text='Подтвержденная электронная почта')

    group = models.ForeignKey(
        'EmployeeGroup', related_name='employee_group',
        on_delete=models.PROTECT, blank=True, null=True,
        help_text='Группа сотрудника')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return super(Employee, self).__str__()


class EmployeeGroup(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Имя группы',
        help_text='Имя группы')
    description = models.CharField(
        max_length=300, verbose_name='Описание',
        help_text='Описание группы')
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        help_text='Дата создания группы')
    creator = models.ForeignKey(
        Employee, related_name='employee_group',
        on_delete=models.PROTECT, blank=True, null=True,
        help_text='Создатель группы')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name
