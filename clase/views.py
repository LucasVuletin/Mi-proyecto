from django.http import HttpResponse
from django.shortcuts import render
from clase.models import curso 
import random
# Create your views here.

def nuevo_curso(request):
    camada = random.randrange(1500,3000)
    nuevo_curso = curso(nombre='curso 35', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f'Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}')