from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{10}$',
    message="Номер должен быть в формате '9633609225'")


class Storage(models.Model):
    name = models.CharField(
        max_length=50, verbose_name='Наименование склада',
        help_text='Store name')
    address = models.CharField(
        max_length=100, verbose_name='Address',
        help_text='Адрес склада')
    mode = models.CharField(
        max_length=200, verbose_name='Mode',
        help_text='Режим работы')
    first_name = models.CharField(
        blank=True, max_length=20, verbose_name='Имя контактного лица',
        help_text='First name contact person')

    middle_name = models.CharField(
        blank=True, max_length=20, verbose_name='Отчетство контактного лица',
        help_text='Middle name contact person')

    last_name = models.CharField(
        blank=True, max_length=20, verbose_name='Фамилия контактного лица',
        help_text='Last name contact person')
    phone_number = models.CharField(
        validators=[phone_regex], max_length=10,
        blank=True, verbose_name='Номер мобильного телефона',
        help_text='Phone number')

    scheme = models.ImageField(
        upload_to='tmp/img', blank=True,
        help_text='Driving directions')
    note = models.CharField(
        max_length=300, verbose_name='Примечание',
        help_text='Note')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.name
