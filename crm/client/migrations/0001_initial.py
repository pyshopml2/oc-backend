# Generated by Django 2.0.7 on 2018-07-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_ownership', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
