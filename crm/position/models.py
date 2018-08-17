from django.db import models

# Модель должности сотрудника
class Position(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Должность сотрудника'
        verbose_name_plural = 'Должности сотрудников'

    def __str__(self):
        return self.name