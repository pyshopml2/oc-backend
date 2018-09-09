from django.db import models


class Position(models.Model):
    name = models.CharField(
        max_length=50, blank=True,
        verbose_name='Должность', help_text='Job title')

    description = models.CharField(
        max_length=300, blank=True,
        verbose_name='Описание', help_text='Job description')

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'

    def __str__(self):
        return self.name
