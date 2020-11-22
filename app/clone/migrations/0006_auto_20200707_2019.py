# Generated by Django 2.2.3 on 2020-07-07 14:49

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clone', '0005_auto_20200705_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 14, 49, 57, 475682, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 14, 49, 57, 474685, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 7, 7, 14, 49, 57, 475682, tzinfo=utc))),
                ('answer_url', models.ForeignKey(on_delete='CASCADE', to='clone.Answer')),
                ('creator', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
