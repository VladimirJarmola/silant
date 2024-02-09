# Generated by Django 4.2.9 on 2024-02-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deskbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driveaxle',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Модель ведущего моста'),
        ),
        migrations.AlterField(
            model_name='enginemodel',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Модель двигателя'),
        ),
        migrations.AlterField(
            model_name='failurenode',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='recoverymethod',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='steeringaxle',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Модель управляемого моста'),
        ),
        migrations.AlterField(
            model_name='transmissionmodel',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Модель трансмиссии'),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Модель техники'),
        ),
    ]