from pyexpat import model
from django.db import models
#sugiere 2 espacios entre class
# Create your models here.
#CHARFIELD: campo de caracteres
#EMAILFIELD: campo de email


class estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
 

class profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)


class entregable(models.Model):
    nombre = models.CharField(max_length=20)
    fehaDeEntrega = models.DateTimeField()
    entregado = models.BooleanField()


class curso(models.Model):
    nombre = models.CharField(max_length=20)
    camada = models.IntegerField()     