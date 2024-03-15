from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    location = models.CharField(max_length=255, verbose_name="Местоположение")
    operating_hours = models.CharField(max_length=255, verbose_name="Часы работы")

    class Meta:
        verbose_name = "Предприятие"
        verbose_name_plural = "Предприятия"

    def __str__(self):
        return self.name
