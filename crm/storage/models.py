from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{10}$',
    message="Номер должен быть в формате '9633609225'")


class Storage(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    address = models.CharField(max_length=100, verbose_name='Склад')
    mode = models.CharField(max_length=200, verbose_name='Режим работы')
    first_name = models.CharField(
        blank=True, max_length=20, verbose_name='Имя контактного лица')

    middle_name = models.CharField(
        blank=True, max_length=20, verbose_name='Отчетство контактного лица')

    last_name = models.CharField(
        blank=True, max_length=20, verbose_name='Фамилия контактного лица')
    phone_number = models.CharField(
        validators=[phone_regex], max_length=10,
        blank=True, verbose_name='Номер мобильного телефона')

    scheme = models.ImageField(upload_to='tmp/img', blank=True)
    note = models.CharField(max_length=300, verbose_name='Примечание')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return self.name
