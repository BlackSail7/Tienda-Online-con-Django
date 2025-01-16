from django.urls import path
from tienda import views



urlpatterns = [
    
   
    path('tienda/', views.shop, name="Tienda"),
    
    
    

]