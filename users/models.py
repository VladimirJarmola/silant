from django.db import models
from django.contrib.auth.models import AbstractUser


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
        verbose_name_plural = "Сервисные компании"

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    ANONYMOUS = "AN"
    CLIENT = "CL"
    SERVICE = "SE"
    MANAGER = "MG"
    ADMIN = "AD"
    ROLE_CHOISES = [
        (ANONYMOUS, "Пользователь без авторизации"),
        (CLIENT, "Клиент"),
        (SERVICE, "Сервисная организация"),
        (MANAGER, "Менеджер"),
        (ADMIN, "Администратор")
    ]

    user_role = models.CharField(
        max_length=2, choices=ROLE_CHOISES, default=ANONYMOUS, verbose_name="Роль пользователя"
    )

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.username}"
