# Generated by Django 2.2.3 on 2020-07-02 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200702_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='followers',
        ),
    ]