from django.shortcuts import render
from .models import Articulo, OrdenCompra, Proveedor

def inicio(request):
    return render(request, 'compras/index.html')

def listado_ordenes(request):
    
    todas_ordenes = OrdenCompra.objects.all()
    return render(request, 'compras/listado_ordenes.html', {'ordenes': todas_ordenes})

def listado_articulos(request):
    
    productos = Articulo.objects.all()  
    return render(request, 'compras/listado_articulos.html', {'articulos': productos})