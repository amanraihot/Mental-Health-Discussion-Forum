# Generated by Django 2.2.3 on 2020-07-21 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0037_auto_20200720_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='followers',
        ),
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 15, 13, 3, 300115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 15, 13, 3, 303175, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 21, 15, 13, 3, 299117, tzinfo=utc)),
        ),
    ]
