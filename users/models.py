from django.db import models
from django.contrib.auth.models import AbstractUser

from deskbook.models import ServiceCompany


class User(AbstractUser):
    CLIENT = "CL"
    SERVICE = "SE"
    MANAGER = "MG"
    ADMIN = "AD"
    ROLE_CHOISES = [
        (CLIENT, "Клиент"),
        (SERVICE, "Сервисная организация"),
        (MANAGER, "Менеджер"),
        (ADMIN, "Администратор")
    ]

    user_role = models.CharField(
        max_length=2, choices=ROLE_CHOISES, verbose_name="Роль пользователя"
    )

    service_company = models.ForeignKey(
        to=ServiceCompany,
        on_delete=models.SET_DEFAULT,
        verbose_name="Сервисная компания",
        default=None,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        if not self.first_name:
            return f"{self.username}"
        return f"{self.first_name}"
