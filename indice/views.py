from django.shortcuts import render

# Create your views here.


from contextvars import Context
from re import template
from django.http import HttpResponse
import random

from django.template import loader
#Context, Template

def inicio(request):
    return render(request, "indice/index.html", {} )

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo en h1</h1>
                        ''')

def numero_random(request):
    numero = random.randrange(15, 180)
    texto = f'<h1>Tu numero random es: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    #Ese numero se pasa despues de la barra, y se pone eso entre mayor y menor para indicarle a la URL (en URLS)
    texto = f'<h1>Tu numero random es: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    #plantilla = open(r"C:\Users\Lucas Vuletin\Desktop\Mi proyecto\miproyecto\mi plantilla\mi_plantilla.html") #Copy Path en el archivo
    #Debi ponerle una 'r' por delante porque delante de un str determina que no tiene escape... sin importar de lo que va a usar
    #Lo hacemos template... pero debemos indicarle el template de DJANGO
    
    #template = loader.get_template("mi_plantilla.html")

    #template = Template(plantilla.read()) #Para poder leer el archivo debemos hacerle READ para que lea el arhivo entero

    nombre = "jorge"
    apellido = "vuletin"

    lista = [3, 1, 2, 45, 1, 2, 3]

    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre), #Esto lo hago xq no lo permite en HTML
        'lista': lista
    }

    #context = Context(diccionario_de_datos)

    #plantilla_preparada = template.render(diccionario_de_datos) #Genera el archivo que el HTTPRESPONSE va a entender par apoder mostrarlo

    #return HttpResponse(plantilla_preparada) #ENTONCES HICE TODO ESTO PARA QUE LEA EL TEXTO UBICADO EN MI_PLANTILLA.HTML

    #SI QUISIERAMOS CREAR MAS PLANTILLAS DEBERIAMOS CODEAR SIEMPRE
    #LO MISMO ENTONCES UTILIZAMOS UN LOADER. Con este reemplazamos
    #la linea de open y la linea de template
    #Debo ir a setting.templates para cargar la direccion completa
    #Ademas no necesitamos un context... directamente renderizamos el dic
    #Tambien evitariamos plantilla.close()

    #VERSION CON RENDER (aca textie plantilla_preparada y return)
    #seguramente veamos render y no open ni el return
    return render(request, "indice/mi_plantilla.html", diccionario_de_datos)
