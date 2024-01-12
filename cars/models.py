from django.db import models


class Cars(models.Model):
    serial_number_vehicle = models.CharField(verbose_name='Зав. № машины', max_length=32, unique=True, null=False, blank=False)
    vehicle_model = models.CharField(verbose_name='Модель техники', max_length=128, unique=False, null=False, blank=False)

    engine_model = models.CharField(verbose_name='Модель двигателя', max_length=128, unique=False, null=False, blank=False)
    serial_number_of_the_engine = models.CharField(verbose_name='Зав. № двигателя', max_length=32, unique=True, null=False, blank=False)

    transmission_model = models.CharField(verbose_name='Модель трансмиссии', max_length=128, unique=False, null=False, blank=False)
    serial_number_of_the_transmission = models.CharField(verbose_name='Зав. № трансмиссии', max_length=32, unique=True, null=False, blank=False)

    drive_axle_model = models.CharField(verbose_name='Модель ведущего моста', max_length=128, unique=False, null=False, blank=False)
    drive_axle_serial_number = models.CharField(verbose_name='Зав. № ведущего моста', max_length=32, unique=True, null=False, blank=False)

    steering_axle_model = models.CharField(verbose_name='Модель управляемого моста', max_length=128, unique=False, null=False, blank=False)
    serial_number_of_the_steered_axle = models.CharField(verbose_name='Зав. № управляемого моста', max_length=32, unique=True, null=False, blank=False)

    supply_contract = models.CharField(verbose_name='Договор поставки №, дата', max_length=128, unique=False, null=True, blank=True)

    date_shipped_from_factory = models.DateField(verbose_name='Дата отгрузки с завода')

    consignee = models.CharField(verbose_name='Грузополучатель (конечный потребитель)', max_length=128, unique=False, null=False, blank=False)

    delivery_address = models.CharField(verbose_name='Адрес поставки (эксплуатации)', max_length=256, unique=False, null=False, blank=False)

    equipment = models.TextField(verbose_name='Комплектация (доп. опции)', unique=False, null=True, blank=True)

    client =  models.CharField(verbose_name='Клиент', max_length=128, unique=False, null=True, blank=True)

    service_company = models.CharField(verbose_name='Сервисная компания', max_length=128, unique=False, null=False, blank=False)

    class Meta:
        db_table = 'car'
        verbose_name = 'Машину'
        verbose_name_plural = 'Машины'

        
    def __str__(self):
        return f'{self.vehicle_model} - {self.serial_number_vehicle}'
    