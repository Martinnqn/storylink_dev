# Generated by Django 2.2 on 2019-10-01 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20190428_2052'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hascontinuation_2',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='hascontinuation_2',
            name='contStory',
        ),
        migrations.RemoveField(
            model_name='hascontinuation_2',
            name='preStory',
        ),
        migrations.RemoveField(
            model_name='resourcepublication',
            name='link_pub',
        ),
        migrations.RemoveField(
            model_name='resourcepublication',
            name='own_user_link',
        ),
        migrations.AddField(
            model_name='resourcepublication',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='resourcepublication',
            name='title',
            field=models.CharField(default='a Title', max_length=500),
        ),
        migrations.AddField(
            model_name='storypublication',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='storypublication',
            name='storyContinuation',
            field=models.ManyToManyField(through='publications.HasContinuation', to='publications.StoryPublication'),
        ),
        migrations.AddField(
            model_name='storypublication',
            name='title',
            field=models.CharField(default='a Title', max_length=500),
        ),
        migrations.AlterField(
            model_name='hascontinuation',
            name='baseStory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='continuationFrom', to='publications.StoryPublication'),
        ),
        migrations.AlterField(
            model_name='hascontinuation',
            name='contStory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='continuatedBy', to='publications.StoryPublication'),
        ),
        migrations.AlterField(
            model_name='hascontinuation',
            name='date_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='creation_date_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resourcepublication',
            name='date_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resourcepublication',
            name='privacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='resourcepublication',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='storypublication',
            name='date_time',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='storypublication',
            name='privacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='storypublication',
            name='valoration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='storypublication',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='ContinuationStoryPublication',
        ),
        migrations.DeleteModel(
            name='HasContinuation_2',
        ),
    ]
