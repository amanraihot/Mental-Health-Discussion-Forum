# Generated by Django 2.2.3 on 2020-07-07 16:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0007_auto_20200707_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 16, 45, 8, 998024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 16, 45, 8, 998696, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 16, 45, 8, 997709, tzinfo=utc)),
        ),
    ]
