from django.shortcuts import render

from servicios import models


def index(request):
    return render(request, "servicios/index.html")


def cliente_list(request):
    query = models.Cliente.objects.all()
    return render(request, "servicios/cliente_list.html", {"clientes": query})


def servicio_list(request):
    query = models.Servicio.objects.all()
    return render(request, "servicios/servicio_list.html", {"servicios": query})


def pedido_list(request):
    query = models.Pedido.objects.all()
    return render(request, "servicios/pedido_list.html", {"pedidos": query})
