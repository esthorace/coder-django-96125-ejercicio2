from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from servicios.forms import ServicioForm
from servicios.models import Servicio


class ServicioList(ListView):
    model = Servicio


class ServicioDetail(DetailView):
    model = Servicio


class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy("servicio_list")


class ServicioUpdate(UpdateView):
    model = Servicio
    form_class = ServicioForm
    success_url = reverse_lazy("servicio_list")


class ServicioDelete(DeleteView):
    model = Servicio
    success_url = reverse_lazy("servicio_list")
