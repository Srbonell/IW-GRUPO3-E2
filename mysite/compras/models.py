from django.db import models

# Create your models here.
from django.db import models

# Entidad para gestionar los proveedores de la empresa 
class Proveedor(models.Model):
    cif = models.CharField(max_length=9, unique=True) 
    nombre_comercial = models.CharField(max_length=150) 
    email = models.EmailField() 
    telefono = models.CharField(max_length=15) 
    direccion = models.TextField() 

    def __str__(self):
        return self.nombre_comercial

# Entidad para el catálogo de artículos industriales 
class Articulo(models.Model):
    codigo = models.CharField(max_length=20, unique=True) 
    nombre = models.CharField(max_length=150) 
    descripcion = models.TextField() 
    categoria = models.CharField(max_length=100) 
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.nombre

# Entidad principal: Órdenes de compra internas
class OrdenCompra(models.Model):
    # Definición de estados para la trazabilidad 
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('recibida', 'Recibida'),
    ]
    
    numero_orden = models.CharField(max_length=50, unique=True)
    fecha_solicitud = models.DateField(auto_now_add=True) 
    fecha_prevista_recepcion = models.DateField() 
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    prioridad = models.CharField(max_length=10) 
    departamento_solicitante = models.CharField(max_length=100) 
    observaciones = models.TextField(blank=True, null=True) 
    
    # Relación 1:N - Una orden pertenece a un proveedor 
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) 
    
    # Relación N:N - Una orden puede tener varios artículos y viceversa
    articulos = models.ManyToManyField(Articulo) 

    def __str__(self):
        return f"Orden {self.numero_orden}"