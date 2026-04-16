from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from servicios.forms import ClienteForm
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


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("cliente_list")


class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy("cliente_list")
