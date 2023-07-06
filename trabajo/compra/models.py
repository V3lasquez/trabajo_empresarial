from django.db import models

# Create your models here.
from django.db import models

class Empleado(models.Model):
    id=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"
    
class Proveedor(models.Model):
    id=models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    direccion =models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    id= models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class OrdenCompra(models.Model):
    id= models.CharField(primary_key=True, max_length=6)
    num_compra = models.CharField(max_length=20)
    fec_emision = models.DateField()
    cantidad = models.PositiveIntegerField()
    prec_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    
    def __str__(self):
        return f" {self.total}"
   
class Pago(models.Model):
    id= models.CharField(primary_key=True, max_length=6)
    fec_pago = models.DateField()
    descuento = models.DecimalField(max_digits=8, decimal_places=2)
    met_pago = models.CharField(max_length=30)
    num_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.fec_pago}, {self.descuento}, {self.num_compra}"