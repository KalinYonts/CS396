# Generated by Django 3.2.8 on 2021-10-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_event_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Calendar', 'verbose_name_plural': 'Calendar'},
        ),
        migrations.AlterField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Location'),
        ),
    ]
