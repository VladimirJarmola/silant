from django.db import models

from deskbook.models import DriveAxle, EngineModel, TransmissionModel, VehicleModel, SteeringAxle


class ServiceCompany(models.Model):
    name = models.CharField(
        verbose_name="Название", max_length=256, unique=True, null=False, blank=False
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "service"
        verbose_name = "Сервисная компания"
        verbose_name_plural = "Сревисные компании"

    def __str__(self):
        return f"{self.name}"


class Cars(models.Model):
    serial_number_vehicle = models.CharField(
        verbose_name="Зав. № машины",
        max_length=32,
        unique=True,
        null=False,
        blank=False,
    )
    vehicle_model = models.ForeignKey(
        to=VehicleModel,
        on_delete=models.SET_DEFAULT,
        default="Не назначено",
        verbose_name="Модель техники",
    )

    engine_model = models.ForeignKey(
        to=EngineModel,
        on_delete=models.SET_DEFAULT,
        default="Не назначено",
        verbose_name="Модель двигателя",
    )
    serial_number_of_the_engine = models.CharField(
        verbose_name="Зав. № двигателя",
        max_length=32,
        unique=True,
        null=False,
        blank=False,
    )

    transmission_model = models.ForeignKey(
        to=TransmissionModel,
        on_delete=models.SET_DEFAULT,
        default="Не назначено",
        verbose_name="Модель трансмиссии",
    )
    serial_number_of_the_transmission = models.CharField(
        verbose_name="Зав. № трансмиссии",
        max_length=32,
        unique=True,
        null=False,
        blank=False,
    )

    drive_axle_model = models.ForeignKey(
        to=DriveAxle,
        on_delete=models.SET_DEFAULT,
        default="Не назначено",
        verbose_name="Модель ведущего моста",
    )
    drive_axle_serial_number = models.CharField(
        verbose_name="Зав. № ведущего моста",
        max_length=32,
        unique=True,
        null=False,
        blank=False,
    )

    steering_axle_model = models.ForeignKey(
        to=SteeringAxle,
        on_delete=models.SET_DEFAULT,
        default="Не назначено",
        verbose_name="Модель управляемого моста",
    )
    serial_number_of_the_steered_axle = models.CharField(
        verbose_name="Зав. № управляемого моста",
        max_length=32,
        unique=True,
        null=False,
        blank=False,
    )

    supply_contract = models.CharField(
        verbose_name="Договор поставки №, дата",
        max_length=128,
        unique=False,
        null=True,
        blank=True,
    )

    date_shipped_from_factory = models.DateField(verbose_name="Дата отгрузки с завода")

    consignee = models.CharField(
        verbose_name="Грузополучатель (конечный потребитель)",
        max_length=128,
        unique=False,
        null=False,
        blank=False,
    )

    delivery_address = models.CharField(
        verbose_name="Адрес поставки (эксплуатации)",
        max_length=256,
        unique=False,
        null=False,
        blank=False,
    )

    equipment = models.TextField(
        verbose_name="Комплектация (доп. опции)", unique=False, null=True, blank=True
    )

    client = models.CharField(
        verbose_name="Клиент", max_length=128, unique=False, null=True, blank=True
    )

    service_company = models.ForeignKey(
        to=ServiceCompany,
        on_delete=models.SET_DEFAULT,
        default="Не назначено",
        verbose_name="Сервисная компания",
    )

    class Meta:
        db_table = "car"
        verbose_name = "Машину"
        verbose_name_plural = "Машины"
        # сортировка по дате отгрузки
        ordering = ('engine_model',)

    def __str__(self):
        return f"{self.serial_number_vehicle} - {self.vehicle_model}"
