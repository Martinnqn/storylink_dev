# Generated by Django 2.2 on 2020-04-17 12:44

import apps.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200415_1606'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', apps.users.models.CustomUserManager()),
            ],
        ),
    ]
