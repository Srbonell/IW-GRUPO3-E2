from django.shortcuts import render,get_object_or_404
from .models import Articulo, OrdenCompra


from django.shortcuts import render, get_object_or_404, redirect

from .models import Proveedor, Articulo, OrdenCompra, DetalleOrden

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

from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProveedorForm

# CREAR PROVEEDOR
def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compras:listado_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'compras/form_proveedor.html', {'form': form})

# ELIMINAR PROVEEDOR
def eliminar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('compras:listado_proveedores')
    return render(request, 'compras/confirmar_borrado.html', {'objeto': proveedor})

#EDITAR PROVEEDOR
def editar_proveedor(request, pk):
    # 1. Buscamos el proveedor o lanzamos error 404 si no existe
    proveedor = get_object_or_404(Proveedor, pk=pk)
    
    if request.method == 'POST':
        # 2. Si enviamos el formulario, pasamos los datos nuevos y la instancia actual
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('compras:listado_proveedores')
    else:
        # 3. Si solo entramos a la página, cargamos el formulario con los datos del proveedor
        form = ProveedorForm(instance=proveedor)
        
    return render(request, 'compras/form_proveedor.html', {
        'form': form,
        'editando': True  # Esto nos servirá para cambiar el título en el HTML
    })
from .models import Articulo
from .forms import ArticuloForm,DetalleOrdenForm
# CREAR
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compras:listado_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'compras/form_articulo.html', {'form': form})
# compras/views.py

# compras/views.py

# compras/views.py

def crear_detalle(request, orden_id):
    orden = get_object_or_404(OrdenCompra, pk=orden_id)
    
    if request.method == 'POST':
        form = DetalleOrdenForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.orden = orden
            
            # ASIGNACIÓN AUTOMÁTICA: 
            # Buscamos el precio estimado del artículo seleccionado y lo fijamos
            detalle.precio_unitario_historico = detalle.articulo.precio_estimado
            
            detalle.save()
            return redirect('compras:detalle_orden', orden_id=orden.pk)
    else:
        form = DetalleOrdenForm()
    
    return render(request, 'compras/form_detalle.html', {'form': form, 'orden': orden})
# EDITAR
def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('compras:listado_articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'compras/form_articulo.html', {'form': form, 'editando': True})

# ELIMINAR
def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        return redirect('compras:listado_articulos')
    return render(request, 'compras/confirmar_borrado.html', {'objeto': articulo})
# compras/views.py
from .models import OrdenCompra
from .forms import OrdenCompraForm

# LISTADO
def listado_ordenes(request):
    todas_ordenes = OrdenCompra.objects.all()
    return render(request, 'compras/listado_ordenes.html', {'ordenes': todas_ordenes})

# CREAR
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenCompraForm(request.POST)
        if form.is_valid():
            nueva_orden = form.save()
            # IMPORTANTE: Redirigir al detalle usando el ID de la orden que acabas de crear
            return redirect('compras:detalle_orden', orden_id=nueva_orden.pk)
    else:
        form = OrdenCompraForm()
    return render(request, 'compras/form_orden.html', {'form': form})

# EDITAR
def editar_orden(request, pk):
    orden = get_object_or_404(OrdenCompra, pk=pk)
    if request.method == 'POST':
        form = OrdenCompraForm(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('compras:listado_ordenes')
    else:
        form = OrdenCompraForm(instance=orden)
    return render(request, 'compras/form_orden.html', {'form': form, 'editando': True})

# ELIMINAR
def eliminar_orden(request, pk):
    orden = get_object_or_404(OrdenCompra, pk=pk)
    if request.method == 'POST':
        orden.delete()
        return redirect('compras:listado_ordenes')
    return render(request, 'compras/confirmar_borrado.html', {'objeto': orden})

# compras/views.py

def eliminar_detalle(request, pk):
    # Buscamos la línea que queremos borrar
    detalle = get_object_or_404(DetalleOrden, pk=pk)
    # Guardamos el ID de la orden para poder volver a ella después
    orden_id = detalle.orden.pk
    
    # Solo permitimos borrar si la orden sigue pendiente
    if detalle.orden.estado == 'pendiente':
        detalle.delete()
    
    return redirect('compras:detalle_orden', orden_id=orden_id)