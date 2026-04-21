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

# Entidad para el catálogo de artículos industriales (Información Maestra)
class Articulo(models.Model):
    codigo = models.CharField(max_length=20, unique=True) 
    nombre = models.CharField(max_length=150) 
    descripcion = models.TextField() 
    categoria = models.CharField(max_length=100) 
    precio_estimado = models.DecimalField(max_digits=10, decimal_places=2) 

    def __str__(self):
        return self.nombre

# Entidad principal: Órdenes de compra (Cabecera)
class OrdenCompra(models.Model):
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

    def __str__(self):
        return f"Orden {self.numero_orden}"

# NUEVO MODELO: Línea de Detalle (Vínculo con datos históricos)
#Esto nos va a ayudar a escalar el proyecto.
class DetalleOrden(models.Model):
    orden = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, related_name='detalles')
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario_historico = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.articulo.nombre} en {self.orden.numero_orden}"