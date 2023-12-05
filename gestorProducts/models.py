from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorias(models.Model):
    codigo = models.IntegerField(unique= True)
    nombre = models.CharField(max_length=99)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    codigo = models.IntegerField(unique= True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=99)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)