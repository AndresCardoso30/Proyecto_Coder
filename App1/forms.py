from django import forms

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