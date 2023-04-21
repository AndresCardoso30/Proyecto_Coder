from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

class UsuarioCrear(forms.Form):
    nombre=forms.CharField(max_length=30)
    edad=forms.IntegerField()
    email=forms.EmailField()
    cel=forms.CharField(max_length=50)


class ArticuloCrear(forms.Form):
    nombre=forms.CharField(max_length=40)
    categoria=forms.CharField(max_length=50)
    precio=forms.IntegerField()


class OpinionCrear(forms.Form):
    articulo=forms.CharField(max_length=30)
    comentario=forms.CharField(max_length=500)
    fecha=forms.DateField()


class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contrasena", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contrasena", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar email")
    password1=forms.CharField(label="Contrasena", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contrasena", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts= {k:"" for k in fields}


class MensajeForm(forms.Form):
    emisor = forms.CharField(max_length=30)
    receptor = forms.CharField(max_length=30)
    mensaje = forms.CharField(label="Mensaje", max_length=200)
    
    clave1=forms.CharField(max_length=100)
    clave2=forms.CharField(max_length=100)