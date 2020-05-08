# Generated by Django 2.2 on 2020-05-05 17:12

import apps.users.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0015_auto_20200505_0924'),
        ('users', '0015_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_reported',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='link_img_perfil',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='pub_subscription',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_subscription',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pub_subscription',
            field=models.ManyToManyField(through='users.PubSubscriptionModelAux', to='publications.StoryPublication'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_subscription',
            field=models.ManyToManyField(through='users.UserSubscriptionModelAux', to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='pubsubscriptionmodelaux',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2Pub', to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='link_img_perfil',
            field=models.ImageField(default='gallery/no-img-profile.png', max_length=350, upload_to=apps.users.models.get_upload_path),
        ),
        migrations.AlterField(
            model_name='usersubscriptionmodelaux',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from2To', to='users.UserProfile'),
        ),
        migrations.AlterField(
            model_name='usersubscriptionmodelaux',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to2From', to='users.UserProfile'),
        ),
    ]