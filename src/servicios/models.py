from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    apellido = models.CharField(max_length=100, db_index=True)
    celular = PhoneNumberField()
    domicilio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
