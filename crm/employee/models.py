from django.db import models
from django.core.validators import RegexValidator

class EmployeePosition(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    #role_employee =

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Номер должен быть в формате '9633609225'")
    phone_number = models.CharField(validators=[phone_regex], max_length=10)
    email = models.EmailField()
    login_skype = models.CharField(max_length=50)
    other_contacts = models.CharField(max_length=200)
    confirmed_email = models.BooleanField()
    blocked_account = models.BooleanField()
    group_employment = models

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class GroupEmployee(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    created_date = models.DateField()
    employees = models.ManyToManyField(Employee, related_name='employee')
    creator = models.OneToOneField(Employee, on_delete=models.PROTECT)