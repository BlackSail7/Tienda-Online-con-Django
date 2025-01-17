from django.urls import path
from . import views


app_name="carro"


urlpatterns = [
    
   
    path('tienda/agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('tienda/eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('tienda/restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('tienda/limpiar/', views.limpiar_carro, name="limpiar"),
    
    
    

]