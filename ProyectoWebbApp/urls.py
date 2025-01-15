


from django.urls import path
from ProyectoWebbApp import views
from django.conf import settings
from django.conf.urls.static import static
from Servicios.views import services

urlpatterns = [
    
    path('', views.home, name="Home"),
    path('tienda', views.shop, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contact, name="Contacto"),
    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)