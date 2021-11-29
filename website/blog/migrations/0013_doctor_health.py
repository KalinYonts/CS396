# Generated by Django 3.2.8 on 2021-10-31 16:27

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20211031_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Smith', 'SMITH'), ('Williams', 'WILLIAMS'), ('Kumal', 'KUMAL'), ('Price', 'PRICE'), ('Edwards', 'EDWARDS'), ('Other', 'OTHER')], default='other', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='phone number', max_length=31)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('prescriptions', models.CharField(blank=True, max_length=50, null=True)),
                ('dose', models.IntegerField(blank=True, default=0, null=True)),
                ('dosetime', models.TimeField(help_text='Dose time', verbose_name='Dose time')),
                ('doctor_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.doctor')),
            ],
        ),
    ]
