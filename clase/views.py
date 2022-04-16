from dataclasses import fields
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from clase.models import curso, estudiante, profesor 
from clase.forms import BusquedaCurso, CursoFormulario, EstudianteFormulario
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

def busqueda_curso(request):
    curso_buscado = []
    dato = request.GET.get('partial_curso', None)
    
    if dato is not None:
        #cursos_buscados = curso.objects.filter(curso-dato)
        curso_buscado = curso.objects.filter(nombre__icontains=dato)

    buscador = BusquedaCurso()
    return render(request, "busqueda_curso.html", {'buscador': buscador, 'curso_buscado': curso_buscado}, {'dato': dato})

#CRUD Basico

def listado_estudiantes(request):
    listado_estudiantes = estudiante.objects.all()
    return render(
        request, "listado_estudiantes.html",
        {'listado_estudiantes': listado_estudiantes}
    )    

def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_estudiante = estudiante(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            nuevo_estudiante.save()
            # return render(request, 'listado_estudiantes.html', {})
            return redirect('listado_estudiantes')

    formulario = EstudianteFormulario()
    return render(request, 'crear_estudiante.html', {'formulario': formulario})

def actualizar_estudiante(request, id):
    estudianteid = estudiante.objects.get(id=id)
    

    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            estudiante.nombre = data['nombre'],
            estudiante.apellido = data['apellido'],
            estudiante.email = data['email']
            estudiante.save()
            # return render(request, 'listado_estudiantes.html', {})
            return redirect('listado_estudiantes')

    formulario = EstudianteFormulario(
        initial={
            'nombre': estudiante.nombre,
            'apellido': estudiante.apellido,
            'email': estudiante.email
        }
    )
    return render(request, 'actualizar_estudiante.html', 
    {'formulario': formulario, 'estudiante': estudianteid})

def borrar_estudiante(request, id):    
    estudianteid = estudiante.objects.get(id=id)
    estudianteid.delete()
    return redirect('listado_estudiantes')

#CRUD Clases basadas en listas    

# class profesor(models.Model):
#     nombre = models.CharField(max_length=20)
#     apellido = models.CharField(max_length=30)
#     email = models.EmailField()
#     profesion = models.CharField(max_length=30)

class ProfesorLista(ListView):
    model = profesor
    template_name = 'profesor_list.html'

class ProfesorDetalle(DetailView):
    model = profesor
    template_name = 'profesor_datos.html'

class ProfesorEditar(UpdateView):
    model = profesor
    success_url = 'profesor_editar.html'
    template_name = 'profesor_editar.html'
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ProfesorBorrar(DeleteView):    
    model = profesor
    success_url = 'profesor_borrar.html'  
    template_name = 'profesor_borrar.html' 
