# Generated by Django 2.2 on 2020-04-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200417_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='link_img_perfil',
            field=models.ImageField(default='gallery/no-img-profile.png', max_length=350, upload_to='gallery/profiles'),
        ),
    ]
