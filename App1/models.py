from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    email=models.EmailField()
    cel=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}-{self.email}"
    

class Articulo(models.Model):
    nombre=models.CharField(max_length=40)
    categoria=models.CharField(max_length=50)
    precio=models.IntegerField()

    def __str__(self):
        return f"{self.nombre}--${self.precio}"

class Opiniones(models.Model):
    articulo=models.CharField(max_length=30)
    comentario=models.CharField(max_length=500)
    fecha=models.DateField()

    def __str__(self):
        return f"{self.articulo} ({self.fecha.day}/{self.fecha.month}/{self.fecha.year}): {self.comentario}"
    

