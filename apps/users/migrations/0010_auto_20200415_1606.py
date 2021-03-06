# Generated by Django 2.2 on 2020-04-15 19:06

import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200328_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='description',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='link_img_perfil',
            field=models.ImageField(default='gallery/no-img-profile.png', upload_to='gallery/profiles'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=35, unique=True, validators=[apps.users.models.unique_user]),
        ),
    ]
