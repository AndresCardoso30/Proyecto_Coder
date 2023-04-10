from django.shortcuts import render, HttpResponse
from App1.models import Usuario, Articulo, Opiniones
from App1.forms import *



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
    #articulos=opiniones["articulo"]
    #comentarios=opiniones["comentario"]
    #fecha=opiniones["fecha"]

    return render(request, "mostrar_opiniones.html", {"opiniones": opiniones})







# PARA USO POSTERIOR
#email=informacion['email']
            #emails_existente=Usuario.objects.filter(email__icontains=email)


            #if emails_existente:
                #if email in emails_existente:
                    #nota="Email ya existente."
                    #formulario = UsuarioCrear()
                    #return render(request, "usuario_crear.html", {"nota":nota})
           