from django.db import models
from django.urls import reverse

from cars.models import Cars
from deskbook.models import FailureNode, RecoveryMethod, ServiceCompany

# Create your models here.
class Reclamation(models.Model):
    date_of_refusal = models.DateField(verbose_name="Дата отказа")
    operating_hours = models.IntegerField(verbose_name="Наработка, м/час")
    failure_node = models.ForeignKey(
        to=FailureNode, on_delete=models.SET_DEFAULT, default=None, verbose_name="Узел отказа"
    )
    description_of_failure = models.TextField(
        verbose_name="Описание отказа", unique=False, null=True, blank=True
    )
    recovery_method = models.ForeignKey(
        to=RecoveryMethod,
        on_delete=models.SET_DEFAULT,
        default=None,
        verbose_name="Способ восстановления",
    )
    parts_used = models.TextField(
        verbose_name="Используемые запасные части", unique=False, null=True, blank=True
    )
    restore_date = models.DateField(verbose_name="Дата восстановления")
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
        db_table = "reclamation"
        verbose_name = "Рекламация"
        verbose_name_plural = "Рекламации"
        ordering = ("car",)

    def __str__(self):
        return f"{self.car} - {self.failure_node} - {self.service_company}"
    
    def get_absolute_url(self):
        return reverse("reclamation:reclamation_all")

    def equipment_downtime(self):
        self.delta = self.restore_date - self.date_of_refusal
        return f"{self.delta.days} суток"
        # return f"{self.restore_date - self.date_of_refusal}"
