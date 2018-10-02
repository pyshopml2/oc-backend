from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone

from . import managers
from position.models import Position


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{10}$',
    message="Номер должен быть в формате '9633609225'")

STATUS = (
    ('1', 'Активный'),
    ('2', 'Болен'),
    ('3', 'Командировка'),
    ('4', 'Отпуск'),
    ('5', 'Уволен'),
)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        blank=True, max_length=50, help_text='First name')
    middle_name = models.CharField(
        blank=True, max_length=50, help_text='Middle name')
    last_name = models.CharField(
        blank=True, max_length=50, help_text='Last name')
    email = models.EmailField(
        blank=True, unique=True, help_text='Email')
    user_position = models.ForeignKey(
        Position, related_name='user_position',
        on_delete=models.PROTECT, blank=True,
        null=True, verbose_name='Должность',
        help_text='Position')

    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name='Дата рождения',
        help_text='Date of birth')
    phone_number = models.CharField(
        validators=[phone_regex], max_length=10,
        blank=True, verbose_name='Номер мобильного телефона',
        help_text='Phone number')

    extra_phone_number = models.CharField(
        validators=[phone_regex], max_length=10,
        blank=True, verbose_name='Дополнительный номер',
        help_text='Extra phone number')

    other_contacts = models.CharField(
        max_length=200, blank=True,
        verbose_name='Дополнительные контакты',
        help_text='Additional contacts')

    timezone = models.DateTimeField(
        default=timezone.now, blank=True,
        null=True, verbose_name='Часовой пояс',
        help_text='Time zone')

    is_active = models.BooleanField(
        default=True, verbose_name='Активный аккаунт',
        help_text='Active account')

    is_staff = models.BooleanField(
        default=False, verbose_name='Статус персонала',
        help_text='Staff Status')

    is_superuser = models.BooleanField(
        default=False, verbose_name='Статус администратора',
        help_text='Admin status')

    confirmed_email = models.BooleanField(
        default=False, verbose_name='Подтвержденный email',
        help_text='Confirmed email')

    status = models.CharField(
        max_length=1, null=True,
        choices=STATUS, default='1',
        help_text='Status')

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def email_user(self, subject, message, from_email='exampl@gmail.com'):
        send_mail(subject, message, from_email, ['exampl@gmail.com'])

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


