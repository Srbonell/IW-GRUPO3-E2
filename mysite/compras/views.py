from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def inicio(request):
    return render(request, 'compras/index.html')

def listado_ordenes(request):
    
    return render(request, 'compras/listado_ordenes.html')

def listado_articulos(request):
    return render(request, 'compras/listado_articulos.html')