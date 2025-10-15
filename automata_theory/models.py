from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from datetime import date
import uuid


class Group(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название группы", unique=True)
    
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        (0, "Преподаватель"),
        (1, "Ученик"),
    ]

    first_name = models.TextField(blank=True, verbose_name="Имя")
    last_name = models.TextField(blank=True, verbose_name="Фамилия")
    role = models.IntegerField(
        blank=False, verbose_name="Роль пользователя", choices=ROLE_CHOICES, default=1
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("user-profile", kwargs={"username": self.username})

    def get_update_url(self):
        return reverse("update_profile", kwargs={"username": self.username})

    def get_delete_url(self):
        return reverse("post_delete_url", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if self.role == 0:
            self.is_superuser = True
        else:
            self.is_superuser = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.group.name if self.group else ""


class KRTime(models.Model):
    KR_CHOICES = [
        (1, "Контрольная работа №1"),
        (2, "Контрольная работа №2"),
        (3, "Контрольная работа №3"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kr_number = models.IntegerField(
        choices=KR_CHOICES, verbose_name="Номер контрольной работы"
    )
    duration = models.DurationField(
        verbose_name="Длительность контрольной работы", default="01:30:00"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активна ли запись")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Время контрольной работы"
        verbose_name_plural = "Время контрольных работ"
        ordering = ["kr_number"]

    def __str__(self):
        return f"КР №{self.kr_number} (Длительность: {self.duration})"
