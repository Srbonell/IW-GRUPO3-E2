from django.urls import path
from . import views


app_name = 'compras'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ordenes/', views.listado_ordenes, name='listado_ordenes'),
    path('articulos/', views.listado_articulos, name='listado_articulos'),
    path('proveedores/', views.listado_proveedores, name='listado_proveedores'),
    path('ordenes/<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
]