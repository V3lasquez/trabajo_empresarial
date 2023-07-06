from django.contrib import admin
from .models import Empleado,Proveedor, Producto, OrdenCompra, Pago
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(OrdenCompra)
admin.site.register(Pago)
