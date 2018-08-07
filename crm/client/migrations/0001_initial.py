# Generated by Django 2.0.7 on 2018-08-07 12:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_auto_20180807_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование организации')),
                ('other_names', models.CharField(blank=True, max_length=255, verbose_name='Другие наименования')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('zip_code', models.CharField(max_length=6)),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Почтовый адрес')),
                ('region', models.CharField(blank=True, max_length=255, verbose_name='Регион')),
                ('city', models.CharField(max_length=255, verbose_name='Населенный пункт')),
                ('website', models.CharField(blank=True, max_length=255, verbose_name='Населенный пункт')),
                ('timezone', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Часовой пояс')),
                ('additional_info', models.CharField(blank=True, max_length=255, verbose_name='Дополнительная информация')),
                ('note', models.TextField(blank=True, verbose_name='Примечание сотрудника')),
                ('date_of_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_of_edit', models.DateField(auto_now=True, verbose_name='Дата последнего редактирования')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный аккаунт')),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='user.Employee', verbose_name='Создатель')),
                ('responsible_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manager', to='user.Employee', verbose_name='Ответственный менеджер')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
