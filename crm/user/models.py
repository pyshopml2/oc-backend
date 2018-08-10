from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group as GroupUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from . import managers
from django.core.mail import send_mail


# Валидация номера телефона
phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Номер должен быть в формате '9633609225'")

STATUS = (
    ('А', 'Активный'),
    ('Б', 'Болен'),
    ('К', 'Командировка'),
    ('О', 'Отпуск'),
    ('У', 'Уволен'),
)

# Модель должности сотрудника
class EmployeePosition(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'

# Модель пользователя
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(blank=True, max_length=20)
    middle_name = models.CharField(blank=True, max_length=20)
    last_name = models.CharField(blank=True, max_length=20)
    email = models.EmailField(blank=True, unique=True)
    role = models.OneToOneField(EmployeePosition, models.PROTECT, blank=True, null=True, verbose_name='Должность')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True,
                                    verbose_name='Номер мобильного телефона')
    extra_phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True,
                                          verbose_name='Дополнительный номер')
    other_contacts = models.CharField(max_length=200, blank=True, verbose_name='Дополнительные контакты')

    timezone = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name='Часовой пояс')

    is_active = models.BooleanField(default=True, verbose_name='Активный аккаунт')
    is_staff = models.BooleanField(default=False, verbose_name='Статус персонала')
    is_superuser = models.BooleanField(default=False, verbose_name='Статус администратора')

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # Отправка письма пользователю
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

# Модель сотрудника
class Employee(User):
    login_skype = models.CharField(max_length=50, blank=True, verbose_name='Skype')
    confirmed_email = models.BooleanField(default=False, verbose_name='Подтвержденный email')
    group = models.OneToOneField('GroupEmployee', on_delete=models.PROTECT, default=None, blank=True, null=True)
    status = models.CharField(max_length=2, null=True, choices=STATUS, default='A')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

# КОнтактное лицо
class ContactPerson(User):
    region = models.CharField(blank=True, max_length=60, verbose_name='Регион')
    city = models.CharField(blank=True, max_length=60, verbose_name='Город')
    dialing_code = models.CharField(max_length=10, verbose_name='Телефонный код города')
    status = models.CharField(max_length=2, null=True, choices=STATUS, default='A')


    class Meta:
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактные лица'

# Модель группы сотрудников
class GroupEmployee(models.Model):
    name = models.CharField(max_length=60, verbose_name='Имя группы')
    description = models.CharField(max_length=400, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    creator = models.CharField(max_length=5, verbose_name='Создатель')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'