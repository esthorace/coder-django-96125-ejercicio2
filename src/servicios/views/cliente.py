from django.views.generic import ListView

from servicios.models import Cliente


class ClienteList(ListView):
    model = Cliente
    # template_name = "servicios/pedido_list.html"
    # context_object_name = "clientes"
