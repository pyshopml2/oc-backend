from django.db import models
from user.models import User
from client.models import Client


class ContactPerson(User):
    region = models.CharField(
        blank=True, max_length=100,
        verbose_name='Регион', help_text='Регион')

    city = models.CharField(
        blank=True, max_length=100, verbose_name='Город',
        help_text='Город')
    dialing_code = models.CharField(
        max_length=10, verbose_name='Телефонный код города',
        help_text='Код города')

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE,
        related_name='contact_person', verbose_name='Компания',
        blank=True, null=True, help_text='Клиент (компания)')

    class Meta:
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактные лица'
