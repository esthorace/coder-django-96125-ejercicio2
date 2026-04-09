from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    apellido = models.CharField(max_length=100, db_index=True)
    celular = PhoneNumberField(unique=True)
    email = models.EmailField(null=True, blank=True)
    domicilio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


class Servicio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        EN_PROGRESO = "en_progreso", "En Progreso"
        COMPLETADO = "completado", "Completado"

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    precio_acordado = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    descripcion = models.TextField(null=True, blank=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )

    def __str__(self):
        return f"Pedido #{self.pk} — {self.cliente} ({self.estado})"
