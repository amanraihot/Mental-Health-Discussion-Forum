# Generated by Django 2.2.3 on 2020-07-15 14:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0026_auto_20200713_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 14, 40, 8, 372470, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 14, 40, 8, 376459, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 15, 14, 40, 8, 372470, tzinfo=utc)),
        ),
    ]