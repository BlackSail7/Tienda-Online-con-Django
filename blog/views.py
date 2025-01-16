from django.shortcuts import render
from blog.models import *


# Create your views here.

def blog(request):


    posts=Post.objects.all()
    categorias=Categorias.objects.all()

    return render(request, "blog/blog.html", {"posts":posts, "categorias":categorias})



def categoria(request, categoria_id):

    
    categoria=Categorias.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)

    return render(request, "blog/categorias.html", {"posts":posts, "categoria":categoria})