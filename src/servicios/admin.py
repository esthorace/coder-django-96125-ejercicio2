from django.contrib import admin

from servicios import models


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "celular")
    search_fields = ("apellido", "nombre", "celular")
    ordering = ("apellido", "nombre")


@admin.register(models.Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "disponible")
    list_filter = ("disponible",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
