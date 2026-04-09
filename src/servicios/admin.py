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


@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "cliente",
        "servicio",
        "precio_acordado",
        "fecha_solicitud",
        "estado",
        "fecha_finalizacion",
    )
    list_filter = ("estado", "fecha_solicitud")
    search_fields = ("cliente__nombre", "servicio__nombre")
    ordering = ("-fecha_solicitud",)
    date_hierarchy = "fecha_solicitud"
