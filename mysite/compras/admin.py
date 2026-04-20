from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Proveedor, Articulo, OrdenCompra 

admin.site.register(Proveedor) 
admin.site.register(Articulo) 
admin.site.register(OrdenCompra) 