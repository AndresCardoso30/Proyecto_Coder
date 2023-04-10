from django.contrib import admin
from django.urls import path, include
from App1.views import *


urlpatterns = [
    path('usuario_crear', usuario_crear, name="crear_usuario"),
    path('crear_articulo', crear_articulo, name="crear_articulo"),
    path('buscar_articulo', busqueda_productos, name='buscar'),
    path('opinion_crear', crear_opinion, name='opinion_crear'),
    path("opiniones", mostrar_opinion, name="opiniones"),
    
    
]