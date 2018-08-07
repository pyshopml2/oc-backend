from django.db import models
from django.utils import timezone
from user.models import Employee, User

class ClientStatus(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Статус клиента'
        verbose_name_plural = 'Статусы клиентов'

class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование организации')
    other_names = models.CharField(max_length=255, blank=True, verbose_name='Другие наименования')
    zip_code = models.CharField(max_length=6)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True, verbose_name='Почтовый адрес')
    region = models.CharField(max_length=255, blank=True, verbose_name='Регион')
    city = models.CharField(max_length=255, verbose_name='Населенный пункт')
    website = models.CharField(max_length=255, blank=True, verbose_name='Сайт')
    timezone = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name='Часовой пояс')

    additional_info = models.CharField(max_length=255, blank=True, verbose_name='Дополнительная информация')
    note = models.TextField(blank=True, verbose_name='Примечание сотрудника')

    client_manager = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='client_manager', blank=True,
                                       null=True, verbose_name='Ответственный менеджер')

    status = models.OneToOneField(ClientStatus, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Статус')
    client_creator = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='client_creator', blank=True,
                                       null=True, verbose_name='Создатель')
    group = models.ManyToManyField('GroupClient')

    date_of_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_of_edit = models.DateField(auto_now=True, verbose_name='Дата последнего редактирования')

    is_active = models.BooleanField(default=True, verbose_name='Активный аккаунт')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class GroupClient(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=400, verbose_name='Описание')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    creator = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='group_client_creator', blank=True,
                                       null=True, verbose_name='Создатель')

    class Meta:
        verbose_name = 'Группа клиента'
        verbose_name_plural = 'Группы клиентов'