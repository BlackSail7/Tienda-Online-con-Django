
from django.urls import path

from django.conf import settings

from .views import *



urlpatterns = [
    

    path('autenticacion/', VRegistro.as_view(), name="autenticacion"),
    path('logout/',cerrar_sesion, name="logout"),
    path('autenticacion/login/',logear, name="login"),


    

]

