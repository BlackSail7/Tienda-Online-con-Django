
from django.shortcuts import HttpResponse, render

from Servicios.models import Servicio

# Create your views here.

def home(request):
    
    return render(request, "ProyectoWebbApp/home.html")





def shop(request):
    
    return render(request, "ProyectoWebbApp/tienda.html")


def blog(request):
    
    return render(request, "ProyectoWebbApp/blog.html")


def contact(request):
    
   return render(request, "ProyectoWebbApp/contacto.html")
