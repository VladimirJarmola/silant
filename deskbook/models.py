from django.db import models


class VehicleModel(models.Model):
    name = models.CharField(
        verbose_name="Модель техники",
        max_length=128,
        unique=False,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "vehicle_model"
        verbose_name = "Модель техники"
        verbose_name_plural = "Модели техники"

    def __str__(self):
        return f"{self.name}"


class EngineModel(models.Model):
    name = models.CharField(
        verbose_name="Модель двигателя",
        max_length=128,
        unique=False,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "engine_model"
        verbose_name = "Модель двигателя"
        verbose_name_plural = "Модели двигателя"

    def __str__(self):
        return f"{self.name}"


class TransmissionModel(models.Model):
    name = models.CharField(
        verbose_name="Модель трансмиссии",
        max_length=128,
        unique=False,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "transmission_model"
        verbose_name = "Модель трансмиссии"
        verbose_name_plural = "Модели трансмиссии"

    def __str__(self):
        return f"{self.name}" 
     

class DriveAxle(models.Model):
    name = models.CharField(
        verbose_name="Модель ведущего моста",
        max_length=128,
        unique=False,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "drive_axle_model"
        verbose_name = "Модель ведущего моста"
        verbose_name_plural = "Модели ведущего моста"

    def __str__(self):
        return f"{self.name}"


class SteeringAxle(models.Model):
    name = models.CharField(
        verbose_name="Модель управляемого моста",
        max_length=128,
        unique=False,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "steering_axle_model"
        verbose_name = "Модель управляемого моста"
        verbose_name_plural = "Модели управляемого моста"

    def __str__(self):
        return f"{self.name}"

class FailureNode(models.Model):
    name = models.CharField(
        verbose_name="Название", max_length=256, unique=False, null=False, blank=False
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "failure_node"
        verbose_name = "Узел отказа"
        verbose_name_plural = "Узлы отказа"

    def __str__(self):
        return f"{self.name}"


class RecoveryMethod(models.Model):
    name = models.CharField(
        verbose_name="Название", max_length=256, unique=False, null=False, blank=False
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "recovery_method"
        verbose_name = "Способ востановления"
        verbose_name_plural = "Способы восстановления"

    def __str__(self):
        return f"{self.name}"


class ViewMaintenance(models.Model):
    name = models.CharField(
        verbose_name="Название", max_length=256, unique=True, null=False, blank=False
    )
    description = models.TextField(
        verbose_name="Описание", unique=False, null=True, blank=True
    )

    class Meta:
        db_table = "view_maintenance"
        verbose_name = "Вид ТО"
        verbose_name_plural = "Виды ТО"

    def __str__(self):
        return f"{self.name}"
