from django.shortcuts import render,get_object_or_404
from .models import Articulo, OrdenCompra

def inicio(request):
    return render(request, 'compras/index.html')

def listado_ordenes(request):
    
    todas_ordenes = OrdenCompra.objects.all()
    return render(request, 'compras/listado_ordenes.html', {'ordenes': todas_ordenes})

def listado_articulos(request):
    
    productos = Articulo.objects.all()  
    return render(request, 'compras/listado_articulos.html', {'articulos': productos})

def detalle_orden(request, orden_id):
    # Buscamos la orden por su ID o devolvemos un error 404 si no existe
    orden = get_object_or_404(OrdenCompra, pk=orden_id)
    return render(request, 'compras/detalle_orden.html', {'orden': orden})