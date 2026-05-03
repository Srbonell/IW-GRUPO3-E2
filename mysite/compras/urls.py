# compras/urls.py
from django.urls import path
from . import views

app_name = 'compras'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ordenes/', views.listado_ordenes, name='listado_ordenes'),
    path('articulos/', views.listado_articulos, name='listado_articulos'),
    path('proveedores/', views.listado_proveedores, name='listado_proveedores'),
    path('ordenes/<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('proveedores/nuevo/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedores/eliminar/<int:pk>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/editar/<int:pk>/', views.editar_proveedor, name='editar_proveedor'),
    path('articulos/nuevo/', views.crear_articulo, name='crear_articulo'),
    path('articulos/editar/<int:pk>/', views.editar_articulo, name='editar_articulo'),
    path('articulos/eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
    path('ordenes/', views.listado_ordenes, name='listado_ordenes'),
    path('ordenes/nueva/', views.crear_orden, name='crear_orden'),
    path('ordenes/editar/<int:pk>/', views.editar_orden, name='editar_orden'),
    path('ordenes/eliminar/<int:pk>/', views.eliminar_orden, name='eliminar_orden'),
    path('ordenes/<int:orden_id>/nuevo-articulo/', views.crear_detalle, name='crear_detalle'),
    path('detalle/eliminar/<int:pk>/', views.eliminar_detalle, name='eliminar_detalle'),
]