from django.urls import path
from blog import views



urlpatterns = [
  
  path('blog/', views.blog, name="Blog"),
  path('blog/categoria/<categoria_id>', views.categoria, name="categorias"),
    

]