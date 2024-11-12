from django.db import models

# Create your models here.

from django.db import models

class Productos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField()  
    imagen = models.ImageField(upload_to='images/')  

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    usuario = models.CharField(primary_key=True, max_length=50)  
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=49)
    direccion = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre  
