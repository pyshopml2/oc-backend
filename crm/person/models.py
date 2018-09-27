from django.db import models

from user.models import User
from client.models import Client


class ContactPerson(User):
    region = models.CharField(
        blank=True, max_length=100,
        verbose_name='Регион', help_text='Region')

    city = models.CharField(
        blank=True, max_length=100, verbose_name='City',
        help_text='Город')
    dialing_code = models.CharField(
        max_length=10, verbose_name='Dialing code',
        help_text='Код города')

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE,
        related_name='contact_person', verbose_name='Компания',
        blank=True, null=True, help_text='Client (company)')

    class Meta:
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактные лица'


# TODO Groups