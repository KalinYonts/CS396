# Generated by Django 3.1.13 on 2021-11-26 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0007_auto_20211126_0558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='day',
        ),
    ]
