from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from compra import views as app_views

urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', views.casa, name='casa'),
    path('proveedores/', views.homeproveedor, name='proveedores'),
    path('registrarproveedor', views.registrarproveedor),
    path('proveedores/edicionproveedor/<id>', views.edicionproveedor),
    path('editarproveedor', views.editarproveedor),
    path('proveedores/eliminarproveedor/<id>', views.eliminarproveedor),
    path('proveedores/verproducto/<id>', views.verproducto, name="verproducto"),
    
    path('empleados/', views.homeempleado, name='empleados'),
    path('registrarempleado', views.registrarempleado),
    path('empleados/edicionempleado/<id>', views.edicionempleado),
    path('editarempleado', views.editarempleado),
    path('empleados/eliminarempleado/<id>', views.eliminarempleado),
    
    path('productos/', views.homeproducto, name='productos'),
    path('registrarproducto', views.registrarproducto),
    path('productos/edicionproducto/<id>', views.edicionproducto),
    path('editarproducto', views.editarproducto),
    path('productos/eliminarproducto/<id>', views.eliminarproducto),
    
    path('ordencompra/', views.homecompra, name='ordencompra'),
    path('registrarordencompra', views.registrarordencompra, name='registrarordencompra'),
    path('ordencompra/eliminarcompra/<id>', views.eliminarcompra),
    
    path('pagos/', views.homepago, name='pagos'),
    path('registrarpago', views.registrarpago, name='registrarpago'),
    
    
    
    path('reporte-pdf/', views.reporte_pdf, name='reporte_pdf'),
    path('reporte_pago/', views.reportepago, name='reporte_pago'),
    path('reporte_compra/', views.reportecompra, name='reporte_compra'),
]