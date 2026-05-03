from django import forms
from .models import Proveedor, Articulo, OrdenCompra, DetalleOrden

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class OrdenCompraForm(forms.ModelForm):
    class Meta:
        model = OrdenCompra
        # Excluimos fecha_solicitud porque tiene auto_now_add=True
        fields = ['numero_orden', 'fecha_prevista_recepcion', 'estado', 
                  'prioridad', 'departamento_solicitante', 'proveedor', 'observaciones']
        widgets = {
            'fecha_prevista_recepcion': forms.DateInput(attrs={'type': 'date'}),
        }

class DetalleOrdenForm(forms.ModelForm):
    class Meta:
        model = DetalleOrden
        fields = ['articulo', 'cantidad', ]