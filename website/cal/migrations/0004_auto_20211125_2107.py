# Generated by Django 3.1.13 on 2021-11-25 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_auto_20211027_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
