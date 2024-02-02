# Generated by Django 4.2.9 on 2024-01-30 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maintenance', '0001_initial'),
        ('deskbook', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='service_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.servicecompany', verbose_name='Сервисная компания'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='view_maintenance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deskbook.viewmaintenance', verbose_name='Вид ТО'),
        ),
    ]
