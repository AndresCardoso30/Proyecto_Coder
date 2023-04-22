from django.shortcuts import render, HttpResponse, redirect
from App1.models import Usuario, Articulo, Opiniones, Mensaje
from App1.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model

from itertools import chain
from operator import attrgetter




@login_required
def usuario_crear(request):

    if request.method == 'POST':

        formulario= UsuarioCrear(request.POST)
        print(formulario)

        if formulario.is_valid:
            informacion = formulario.cleaned_data               
            usuario = Usuario(nombre=informacion['nombre'], edad=informacion['edad'], email=informacion['email'], cel=informacion['cel'])
            usuario.save()
            return render(request, "usuario_creado.html")
        
    else:
        formulario = UsuarioCrear()

    return render(request, "usuario_crear.html", {"formulario":formulario})

@login_required
def crear_articulo(request):
    if request.method == 'POST':

        formulario=ArticuloCrear(request.POST)
        print(formulario)

        if formulario.is_valid:
            informacion=formulario.cleaned_data
            articulo = Articulo(nombre=informacion['nombre'], categoria=informacion['categoria'], precio=informacion['precio'])
            articulo.save()
            nota="Articulo creado correctamente."
            return render(request, "crear_articulo.html", {"nota":nota})
    
    else:
        formulario = ArticuloCrear()
    
    return render(request, "crear_articulo.html", {"formulario":formulario})

def busqueda_productos(request):
    return render(request, "busqueda_articulos.html")

def buscar(request):

    if request.GET["art"]:
        
        articulo=request.GET["art"]

        articulos=Articulo.objects.filter(nombre__icontains=articulo)
        
        if articulos:
            return render(request, "resultado_busqueda.html", {"articulos":articulos, "query":articulo})
        else: 
            mensaje=f"No existen articulos relacionados a su busqueda: {articulo}."
            return render(request, "resultado_busqueda.html", {"query": articulo, "mensaje":mensaje})

    else:
        mensaje="No has introducido ningun producto."

    
    return render(request, "limpio.html", {"mensaje":mensaje})

@login_required
def crear_opinion(request):

    
    if request.method == 'POST':

        formulario=OpinionCrear(request.POST)
        print(formulario)

        if formulario.is_valid:
            informacion=formulario.cleaned_data
            opinion = Opiniones(articulo=informacion['articulo'], comentario=informacion['comentario'], fecha=informacion['fecha'])
            opinion.save()
            nota="Su opinion se registro correctamente."
            return render(request, "opinion_creada.html", {"nota":nota})
    
    else:
        formulario = OpinionCrear()
    
    return render(request, "opiniones.html", {"formulario":formulario})


def mostrar_opinion(request):

    opiniones=Opiniones.objects.all()

    return render(request, "mostrar_opiniones.html", {"opiniones": opiniones})

@login_required
def eliminar_articulo(request, id):

    articulo=Articulo.objects.get(id=id)
    articulo.delete()
    mensaje="Articulo eliminado correctamente."
    return render(request, "busqueda_articulos.html")

@login_required
def editar_articulo(request, id):
    articulo=Articulo.objects.get(id=id)
    if request.method == "POST":
        formulario=ArticuloCrear(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            articulo.nombre=informacion['nombre']
            articulo.categoria=informacion['categoria']
            articulo.precio=informacion['precio']
            
            articulo.save()
            return render(request, "busqueda_articulos.html")
    
    else:
        formulario=ArticuloCrear(initial={'nombre':articulo.nombre, 'categoria':articulo.categoria, 'precio':articulo.precio})
    
    return render(request, "editar_articulo.html", {'formulario':formulario, 'articulo':articulo})

def login_request(request):

    if request.method == "POST":
        form= AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, 'inicio.html', {"mensaje":f"Bienvenido {usuario}"})
            
            else:

                return render(request, 'login.html', {"mensaje":"Datos ingresados incorrectos"})
            
        else:

            return render(request, "login.html", {"mensaje": "Error, formulario erroneo", "form":form})
        
    form = AuthenticationForm()

    return render(request, "login.html", {"form":form})

def register(request):

    if request.method == "POST":

        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():

            username = form.cleaned_data['username']
            
            form.save()
            return render(request, 'inicio.html', {"mensaje": "Usuario creado correctamente"})
        
    else: 

        form = RegistroUsuarioForm()

    return render (request, "registro.html", {"form": form})    



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, 'inicio.html')
    
    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, 'editar_perfil.html', {"miFormulario":miFormulario, "usuario":usuario})
           

@login_required
def buscar_usuarios(request):
    User = get_user_model()
    users = User.objects.all()

    return render(request, "usuarios.html", {"users":users})

@login_required
def chatear(request, id):
    emisor = request.user
    receptor = User.objects.get(id=id)
    chats = Mensaje.objects.filter(clave1__icontains=emisor.id).filter(clave2__icontains=receptor.id)
    chats_receptor = Mensaje.objects.filter(clave1__icontains=receptor.id).filter(clave2__icontains=emisor.id)

    resultado = sorted(chain(chats, chats_receptor), key=attrgetter('tiempo'))

    clave1=emisor.id
    clave2=receptor.id   

    if chats:
        mensaje=f"Chats con {receptor.username}"
    else:
        mensaje="No hay chats"

    if request.method == "POST":
        
        miFormulario = MensajeForm(request.POST, initial={'emisor':emisor, 'receptor':receptor, 'clave1':clave1, 'clave2':clave2})

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            chat=Mensaje(emisor=informacion['emisor'], receptor=informacion['receptor'], mensaje=informacion['mensaje'], clave1=informacion['clave1'], clave2=informacion['clave2'])
            chat.save()
            chats = Mensaje.objects.filter(clave1__icontains=emisor.id).filter(clave2__icontains=receptor.id)
            chats_receptor = Mensaje.objects.filter(clave1__icontains=receptor.id).filter(clave2__icontains=emisor.id)
            resultado = sorted(chain(chats, chats_receptor), key=attrgetter('tiempo'))
            
            
            

            return render(request, "chat.html", {"miFormulario":miFormulario, "chats":resultado, "mensaje":mensaje})
        
    mensaje2= "Hay errores wey"

    miFormulario = MensajeForm(initial={'emisor':emisor, 'receptor':receptor, 'clave1':clave1, 'clave2':clave2})

    return render(request, "chat.html", {"miFormulario":miFormulario, "mensaje":mensaje, "mensaje2":mensaje2, "chats":resultado})






def mostrar_chat(request, id):
    emisor = request.user
    receptor = User.objects.get(id=id)
    chats = Mensaje.objects.get(clave1=emisor.id, clave2=receptor.id)
    clave1=emisor.id 
    clave2=receptor.id
    miFormulario = MensajeForm(initial={'emisor':emisor, 'receptor':receptor, 'clave1':clave1, 'clave2':clave2})

    return render(request, "chat.html", {"miFormulario":miFormulario, "chats":chats, "receptor":receptor})

    
        
    

    

