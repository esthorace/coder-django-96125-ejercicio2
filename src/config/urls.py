"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from servicios.views import cliente, pedido, servicio

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="servicios/index.html"), name="index"),
    path("cliente/", cliente.ClienteList.as_view(), name="cliente_list"),
    path("cliente/create/", cliente.ClienteCreate.as_view(), name="cliente_create"),
    path("cliente/<int:pk>", cliente.ClienteDetail.as_view(), name="cliente_detail"),
    path(
        "cliente/<int:pk>/delete",
        cliente.ClienteDelete.as_view(),
        name="cliente_delete",
    ),
    path("servicio/", servicio.ServicioList.as_view(), name="servicio_list"),
    path("pedido/", pedido.PedidoList.as_view(), name="pedido_list"),
]
