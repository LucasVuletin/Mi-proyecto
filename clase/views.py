from django.http import HttpResponse
from django.shortcuts import render
from clase.models import curso 
from clase.forms import CursoFormulario
import random
# Create your views here.

def nuevo_curso(request):
    camada = random.randrange(1500,3000)
    nuevo_curso = curso(nombre='curso 35', camada=camada)
    nuevo_curso.save()
    return HttpResponse(f'Se creo el curso {nuevo_curso.nombre} camada {nuevo_curso.camada}')

def formulario_curso(request):
    #Sin formularios de django
    #print(request.method)
    #if request.method == 'POST':
    #    print(request.POST)
    #    nuevo_curso = curso(nombre=request.POST['curso'], camada=request.POST['camada'])
    #    nuevo_curso.save()
    #    return render(request, 'formulario_curso.html', {'nuevo_curso': nuevo_curso})

    #return render(request, 'formulario_curso.html',{})

    #Con formularios de django

    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_curso = curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()
            return render(request, 'indice/index.html', {'nuevo_curso': nuevo_curso})

    formulario = CursoFormulario()
    return render(request, 'formulario_curso.html',{'formulario': formulario})    