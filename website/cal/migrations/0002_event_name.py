# Generated by Django 3.2.8 on 2021-10-27 22:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.TextField(default=django.utils.timezone.now, help_text='name of the event', verbose_name='Name of the Event'),
            preserve_default=False,
        ),
    ]
