import os
import binascii
import uuid
from datetime import datetime, timedelta

from django.db import models
from django.conf import settings

from core.tests.consts import TZ


def get_default_date():
    return datetime.now(tz=TZ) + timedelta(days=1)


class TempToken(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_temp_token',
        on_delete=models.CASCADE, verbose_name="User")
    token = models.CharField(
        max_length=50, verbose_name='Temporary token',
        help_text='Temporary token', primary_key=True)
    active = models.BooleanField(
        verbose_name='Is active?', default=True,
        help_text='Is active?')
    creation_date = models.DateTimeField(
        auto_now=True, verbose_name='Creation date',
        help_text='Creation date')
    expiration_date = models.DateTimeField(
        default=get_default_date,
        verbose_name='Expiration date',
        help_text='Expiration date')

    class Meta:
        verbose_name = 'Temporary token'
        verbose_name_plural = 'Temporary tokens'

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
        return super(TempToken, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.token


class EmailToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='email_token',
                             on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False,
                             verbose_name='Токен для подтверждения email',
                             help_text='Token for confirmation email')