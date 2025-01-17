
from django.urls import path

from django.conf import settings

from .views import VRegistro

urlpatterns = [
    

    path('autenticacion/', VRegistro.as_view(), name="autenticacion"),

    

]

