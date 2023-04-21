from django.db import models
from django.contrib.auth.models import User

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
    


    

class Mensaje(models.Model):
    #canal = models.ForeignKey("Canal", on_delete=models.CASCADE)
    #emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emisor')
    #receptor=models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptor')
    emisor = models.CharField(max_length=30)
    receptor=models.CharField(max_length=30)
    mensaje = models.CharField(max_length=200)
    tiempo = models.DateTimeField(auto_now_add=True)
    clave1= models.CharField(max_length=100)
    clave2= models.CharField(max_length=100)
    #leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mensaje}"
    
    #class Meta:
        #orden = ('tiempo',)

#class CanalUsuario(models.Model):
#    canal = models.ForeignKey("Canal", null=True, on_delete=models.SET_NULL)
#    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


#class Canal(models.Model):
#    usuarios = models.OneToOneField(User, blank=True, through=CanalUsuario)
#


