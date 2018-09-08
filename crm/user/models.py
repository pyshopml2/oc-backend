from django.conf import settings

from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from . import managers
from django.core.mail import send_mail
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
        blank=True, max_length=50, help_text='Имя')
    middle_name = models.CharField(
        blank=True, max_length=50, help_text='Отчество')
    last_name = models.CharField(
        blank=True, max_length=50, help_text='Фамилия')
    email = models.EmailField(
        blank=True, unique=True, help_text='Электронная почта')
    user_position = models.ForeignKey(
        Position, related_name='user_position',
        on_delete=models.PROTECT, blank=True,
        null=True, verbose_name='Должность',
        help_text='Должность')

    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name='Дата рождения',
        help_text='Дата рождения')
    phone_number = models.CharField(
        validators=[phone_regex], max_length=10,
        blank=True, verbose_name='Номер мобильного телефона',
        help_text='Номер мобильного телефона')

    extra_phone_number = models.CharField(
        validators=[phone_regex], max_length=10,
        blank=True, verbose_name='Дополнительный номер',
        help_text='Дополнительный номер')

    other_contacts = models.CharField(
        max_length=200, blank=True,
        verbose_name='Дополнительные контакты',
        help_text='Допонительные контакты')

    timezone = models.DateTimeField(
        default=timezone.now, blank=True,
        null=True, verbose_name='Часовой пояс',
        help_text='Часовой пояс')

    is_active = models.BooleanField(
        default=True, verbose_name='Активный аккаунт',
        help_text='Активный аккаунт')

    is_staff = models.BooleanField(
        default=False, verbose_name='Статус персонала',
        help_text='Статус персонала')

    is_superuser = models.BooleanField(
        default=False, verbose_name='Статус администратора',
        help_text='Статус администратора')

    status = models.CharField(
        max_length=1, null=True,
        choices=STATUS, default='1',
        help_text='Статус')

    objects = managers.UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    # Отправка письма пользователю
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
