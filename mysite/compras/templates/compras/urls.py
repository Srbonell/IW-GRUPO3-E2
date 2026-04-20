from django.urls import path
from views import views


app_name = 'compras'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ordenes/', views.listado_ordenes, name='listado_ordenes'),
    path('articulos/', views.listado_articulos, name='listado_articulos'),
]