from django.shortcuts import redirect, render
from .form import FormularioContacto
from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):  

   formulario_contacto=FormularioContacto()

   if request.method=="POST":
      formulario_contacto=FormularioContacto(data=request.POST)
      if formulario_contacto.is_valid():
         nombre=request.POST.get("nombre")
         email=request.POST.get("email")
         contenido=request.POST.get("contenido")

         email=EmailMessage("Mensaje desde App Django", 
            "El usuario con nombre {} con el email {}  escribre lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["<insert your email>"], reply_to=[email])
         
      try: 

         email.send()

         #return redirect("/contacto/?valido")

         return render(request, "contacto/contactoValido.html")

      except: return render(request, "contacto/contacto.html",{"formulario":formulario_contacto})
    
   return render(request, "contacto/contacto.html",{"formulario":formulario_contacto})









