# Generated by Django 2.2 on 2020-03-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20191204_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='link_img_perfil',
            field=models.ImageField(default='gallery/no-img.jpg', upload_to='gallery/profiles'),
        ),
    ]
