# Generated by Django 2.2.3 on 2020-07-09 17:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0013_auto_20200709_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 1, 38, 5932, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 1, 38, 6892, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 17, 1, 38, 4940, tzinfo=utc)),
        ),
    ]
