# Generated by Django 2.2.3 on 2020-07-16 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0033_auto_20200716_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 16, 31, 30, 32851, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 16, 31, 30, 36841, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 16, 31, 30, 32851, tzinfo=utc)),
        ),
    ]
