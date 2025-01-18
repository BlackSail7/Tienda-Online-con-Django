
from django.shortcuts import HttpResponse, render

from Servicios.models import Servicio
from carro.carro import Carro

# Create your views here.

def home(request):

    carro=Carro(request)
   
    return render(request, "ProyectoWebbApp/home.html")











