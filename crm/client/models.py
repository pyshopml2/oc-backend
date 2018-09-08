from django.db import models
from django.utils import timezone
from employee.models import Employee
from user.models import User


class ClientStatus(models.Model):
    name = models.CharField(
        max_length=50, help_text='Наименование статуса')

    class Meta:
        verbose_name = 'Статус клиента'
        verbose_name_plural = 'Статусы клиентов'

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Наименование организации',
        help_text='Наименование клиента')

    other_names = models.CharField(
        blank=True, max_length=50,
        verbose_name='Другие наименования',
        help_text='Другие наименования клиента')

    zip_code = models.CharField(
        max_length=10, help_text='Почтовый код')

    email = models.EmailField(
        unique=True, help_text='Электронная почта')

    address = models.CharField(
        max_length=100, blank=True,
        verbose_name='Почтовый адрес',
        help_text='Адрес клиента')

    region = models.CharField(
        max_length=100, blank=True,
        verbose_name='Регион', help_text='Регион')

    city = models.CharField(
        max_length=100,
        verbose_name='Населенный пункт', help_text='Город')

    website = models.CharField(
        max_length=50, blank=True,
        verbose_name='Сайт', help_text='Сайт компании')

    timezone = models.DateTimeField(
        default=timezone.now, blank=True,
        null=True, verbose_name='Часовой пояс',
        help_text='Часовой пояс')

    additional_info = models.CharField(
        max_length=300, blank=True,
        verbose_name='Дополнительная информация',
        help_text='Дополнительная информация')

    note = models.TextField(
        blank=True, verbose_name='Примечание сотрудника',
        help_text='Примечание')

    employee_manager = models.ForeignKey(
        Employee, on_delete=models.PROTECT,
        related_name='employee_manager', blank=True,
        null=True, verbose_name='Ответственный менеджер',
        help_text='Ответственный менеджер')

    client_status = models.ForeignKey(
        ClientStatus, on_delete=models.PROTECT,
        related_name='client_status', blank=True,
        null=True, verbose_name='Статус',
        help_text='Статус')

    employee_creator = models.ForeignKey(
        Employee, on_delete=models.PROTECT,
        related_name='employee_creator', blank=True,
        null=True, verbose_name='Создатель',
        help_text='Сотрудник, создавший клиента')

    client_group = models.ManyToManyField(
        'ClientGroup', blank=True,
        related_name='client_group',
        help_text='Группы клиента')

    date_of_create = models.DateField(
        auto_now_add=True, verbose_name='Дата создания',
        help_text='Дата создания')

    date_of_edit = models.DateField(
        auto_now=True, verbose_name='Дата последнего редактирования',
        help_text='Дата последнего редактирования')

    is_active = models.BooleanField(
        default=True, verbose_name='Активный аккаунт',
        help_text='Активный аккаунт')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class ClientGroup(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Название',
        help_text='Наименование группы')

    description = models.CharField(
        max_length=300, verbose_name='Описание',
        help_text='Описание группы')

    created_date = models.DateField(
        auto_now_add=True, verbose_name='Дата создания',
        help_text='Дата создания')

    employee_creator = models.ForeignKey(
        Employee, related_name='client_group',
        blank=True, verbose_name='Создатель',
        on_delete=models.PROTECT, null=True,
        help_text='Создатель группы')

    class Meta:
        verbose_name = 'Группа клиента'
        verbose_name_plural = 'Группы клиентов'

    def __str__(self):
        return self.name
