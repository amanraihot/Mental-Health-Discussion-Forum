# Generated by Django 2.2.3 on 2020-07-08 07:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0009_auto_20200708_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 7, 22, 7, 930664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 7, 22, 7, 930664, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 7, 22, 7, 929667, tzinfo=utc)),
        ),
    ]
