from django import forms

from servicios.models import Cliente, Pedido, Servicio


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = "__all__"
