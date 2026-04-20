from django.db import models

# Create your models here.
from django.db import models

# Entidad para gestionar los proveedores de la empresa [cite: 223, 230]
class Proveedor(models.Model):
    cif = models.CharField(max_length=9, unique=True) # [cite: 231]
    nombre_comercial = models.CharField(max_length=150) # [cite: 232]
    email = models.EmailField() # [cite: 233]
    telefono = models.CharField(max_length=15) # [cite: 234]
    direccion = models.TextField() # [cite: 235]

    def __str__(self):
        return self.nombre_comercial

# Entidad para el catálogo de artículos industriales [cite: 225, 237]
class Articulo(models.Model):
    codigo = models.CharField(max_length=20, unique=True) # [cite: 226]
    nombre = models.CharField(max_length=150) # [cite: 226]
    descripcion = models.TextField() # [cite: 227]
    categoria = models.CharField(max_length=100) # [cite: 228]
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2) # [cite: 229, 760]

    def __str__(self):
        return self.nombre

# Entidad principal: Órdenes de compra internas [cite: 212, 216]
class OrdenCompra(models.Model):
    # Definición de estados para la trazabilidad [cite: 220, 1834]
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('recibida', 'Recibida'),
    ]
    
    numero_orden = models.CharField(max_length=50, unique=True) # [cite: 217]
    fecha_solicitud = models.DateField(auto_now_add=True) # [cite: 218, 1941]
    fecha_prevista_recepcion = models.DateField() # [cite: 219]
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente') # [cite: 220, 1938]
    prioridad = models.CharField(max_length=10) # [cite: 221, 1933]
    departamento_solicitante = models.CharField(max_length=100) # [cite: 222]
    observaciones = models.TextField(blank=True, null=True) # [cite: 224]
    
    # Relación 1:N - Una orden pertenece a un proveedor [cite: 223, 931]
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) 
    
    # Relación N:N - Una orden puede tener varios artículos y viceversa [cite: 240, 932]
    articulos = models.ManyToManyField(Articulo) 

    def __str__(self):
        return f"Orden {self.numero_orden}"