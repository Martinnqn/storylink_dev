# Generated by Django 2.2 on 2020-03-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0006_remove_storypublication_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hashtag',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='resourcepublication',
            old_name='hashtag',
            new_name='tag',
        ),
        migrations.RenameField(
            model_name='storypublication',
            old_name='hashtag',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='storypublication',
            name='user_lastname',
        ),
        migrations.RemoveField(
            model_name='storypublication',
            name='user_name',
        ),
        migrations.AddField(
            model_name='storypublication',
            name='subtitle',
            field=models.CharField(default='oldP', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storypublication',
            name='img_content_link',
            field=models.ImageField(default='gallery/no-img.jpg', upload_to='gallery/publications'),
        ),
        migrations.AlterField(
            model_name='storypublication',
            name='privacity',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='storypublication',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
