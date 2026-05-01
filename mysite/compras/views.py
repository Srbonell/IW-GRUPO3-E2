from django.shortcuts import render,get_object_or_404
from .models import Articulo, OrdenCompra

from django.shortcuts import render
from .models import Articulo, OrdenCompra, Proveedor

def inicio(request):
    # Contamos los registros de cada tabla
    total_articulos = Articulo.objects.count()
    total_ordenes = OrdenCompra.objects.count()
    total_proveedores = Proveedor.objects.count()
    
    # Buscamos las órdenes que están como "Pendiente" para el aviso
    ordenes_pendientes = OrdenCompra.objects.filter(estado='pendiente').count()

    context = {
        'total_articulos': total_articulos,
        'total_ordenes': total_ordenes,
        'total_proveedores': total_proveedores,
        'ordenes_pendientes': ordenes_pendientes,
    }    
    
    return render(request, 'compras/index.html', context)

def listado_proveedores(request):
    todos_proveedores = Proveedor.objects.all()
    return render(request, 'compras/listado_proveedores.html', {'proveedores': todos_proveedores})

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