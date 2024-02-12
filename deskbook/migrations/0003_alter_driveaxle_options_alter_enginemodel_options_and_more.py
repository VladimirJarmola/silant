# Generated by Django 4.2.9 on 2024-02-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deskbook', '0002_alter_driveaxle_name_alter_enginemodel_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driveaxle',
            options={'ordering': ('name',), 'verbose_name': 'Модель ведущего моста', 'verbose_name_plural': 'Модели ведущего моста'},
        ),
        migrations.AlterModelOptions(
            name='enginemodel',
            options={'ordering': ('name',), 'verbose_name': 'Модель двигателя', 'verbose_name_plural': 'Модели двигателя'},
        ),
        migrations.AlterModelOptions(
            name='failurenode',
            options={'ordering': ('name',), 'verbose_name': 'Узел отказа', 'verbose_name_plural': 'Узлы отказа'},
        ),
        migrations.AlterModelOptions(
            name='recoverymethod',
            options={'ordering': ('name',), 'verbose_name': 'Способ востановления', 'verbose_name_plural': 'Способы восстановления'},
        ),
        migrations.AlterModelOptions(
            name='steeringaxle',
            options={'ordering': ('name',), 'verbose_name': 'Модель управляемого моста', 'verbose_name_plural': 'Модели управляемого моста'},
        ),
        migrations.AlterModelOptions(
            name='transmissionmodel',
            options={'ordering': ('name',), 'verbose_name': 'Модель трансмиссии', 'verbose_name_plural': 'Модели трансмиссии'},
        ),
        migrations.AlterModelOptions(
            name='vehiclemodel',
            options={'ordering': ('name',), 'verbose_name': 'Модель техники', 'verbose_name_plural': 'Модели техники'},
        ),
        migrations.AlterModelOptions(
            name='viewmaintenance',
            options={'ordering': ('-name',), 'verbose_name': 'Вид ТО', 'verbose_name_plural': 'Виды ТО'},
        ),
        migrations.AlterField(
            model_name='failurenode',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Узел отказа'),
        ),
        migrations.AlterField(
            model_name='recoverymethod',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Способ востановления'),
        ),
        migrations.AlterField(
            model_name='viewmaintenance',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Вид ТО'),
        ),
    ]
