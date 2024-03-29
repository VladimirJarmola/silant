from django.db import models
from django.urls import reverse

from deskbook.models import ViewMaintenance, ServiceCompany
from cars.models import Cars


# Create your models here.
class Maintenance(models.Model):
    view_maintenance = models.ForeignKey(
        to=ViewMaintenance, on_delete=models.SET_DEFAULT, default=None, verbose_name="Вид ТО"
    )
    Date_maintenance = models.DateField(verbose_name="Дата проведения ТО")
    operating_hours = models.IntegerField(verbose_name="Наработка, м/час")
    work_order_number = models.CharField(
        verbose_name="№ заказ-наряда",
        max_length=128,
        null=False,
        blank=False,
    )
    work_order_date = models.DateField(verbose_name="Дата заказ-наряда")
    # organization = models.CharField(verbose_name='Организация, проводившая ТО', max_length=128, unique=False, null=False, blank=False)
    car = models.ForeignKey(
        to=Cars,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name="Машина",
    )
    service_company = models.ForeignKey(
        to=ServiceCompany,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name="Сервисная компания",
    )

    class Meta:
        db_table = "maintenance"
        verbose_name = "ТО"
        verbose_name_plural = "ТО"
        ordering = ("car",)

    def __str__(self):
        return f"{self.car} - {self.view_maintenance}"
    
    def get_absolute_url(self):
        return reverse("maintenance:maintenance_all")
    
