# Generated by Django 4.2.9 on 2024-02-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='work_order_number',
            field=models.CharField(max_length=128, verbose_name='№ заказ-наряда'),
        ),
    ]