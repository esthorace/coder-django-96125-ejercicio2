from django.contrib import admin

from servicios import models


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "celular")
    search_fields = ("apellido", "nombre", "celular")
    ordering = ("apellido", "nombre")
