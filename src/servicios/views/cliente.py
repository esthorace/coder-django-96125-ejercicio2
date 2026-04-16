from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView

from servicios.models import Cliente


class ClienteList(ListView):
    model = Cliente
    # template_name = "servicios/pedido_list.html"
    # context_object_name = "clientes"


class ClienteDetail(DetailView):
    model = Cliente


class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente_list")
