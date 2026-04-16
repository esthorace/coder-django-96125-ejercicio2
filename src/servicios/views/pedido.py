from django.views.generic import ListView

from servicios.models import Pedido


class PedidoList(ListView):
    model = Pedido
