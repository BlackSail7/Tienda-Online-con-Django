
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from Servicios import views

urlpatterns = [
    

    path('servicios/', views.services, name="Servicios"),

    

]

