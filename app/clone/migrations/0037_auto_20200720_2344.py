# Generated by Django 2.2.3 on 2020-07-20 18:14

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clone', '0036_auto_20200719_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='topics',
            field=models.ManyToManyField(related_name='topic_answers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 18, 14, 22, 763028, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 18, 14, 22, 765019, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 20, 18, 14, 22, 762031, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topics',
            field=models.ManyToManyField(related_name='topic_questions', to='clone.Topics'),
        ),
    ]
