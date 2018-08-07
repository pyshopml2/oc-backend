from django.db import models
from django.utils import timezone
from user.models import Employee, User

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование организации')
    other_names = models.CharField(max_length=255, blank=True, verbose_name='Другие наименования')
    email = models.EmailField(unique=True)
    zip_code = models.CharField(max_length=6)
    address = models.CharField(max_length=255, blank=True, verbose_name='Почтовый адрес')
    region = models.CharField(max_length=255, blank=True, verbose_name='Регион')
    city = models.CharField(max_length=255, verbose_name='Населенный пункт')
    website = models.CharField(max_length=255, blank=True, verbose_name='Населенный пункт')
    timezone = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name='Часовой пояс')
    
    additional_info = models.CharField(max_length=255, blank=True, verbose_name='Дополнительная информация')
    note = models.TextField(blank=True, verbose_name='Примечание сотрудника')

    client_manager = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='client_manager', blank=True, null=True, verbose_name='Ответственный менеджер')
    #status = models.OneToOneField(Status, models.PROTECT, blank=True, null=True, verbose_name='Статус')
    client_creator = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='client_creator', blank=True, null=True, verbose_name='Создатель')

    date_of_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_of_edit = models.DateField(auto_now=True, verbose_name='Дата последнего редактирования')

    is_active = models.BooleanField(default=True, verbose_name='Активный аккаунт')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'