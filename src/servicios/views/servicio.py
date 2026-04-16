from django.views.generic import ListView

from servicios.models import Servicio


class ServicioList(ListView):
    model = Servicio
