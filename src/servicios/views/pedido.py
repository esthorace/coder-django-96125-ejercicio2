from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from servicios.forms import PedidoForm
from servicios.models import Pedido


class PedidoList(ListView):
    model = Pedido


class PedidoDetail(DetailView):
    model = Pedido


class PedidoCreate(CreateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy("pedido_list")


class PedidoUpdate(UpdateView):
    model = Pedido
    form_class = PedidoForm
    success_url = reverse_lazy("pedido_list")


class PedidoDelete(DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedido_list")
