from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular = PhoneNumberField()
    domicilio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
