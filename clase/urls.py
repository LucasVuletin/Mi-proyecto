from django.urls import path
from .views import formulario_curso, nuevo_curso, busqueda_curso
urlpatterns = [
    path('nuevo/', nuevo_curso, name='nuevo_curso'),
    path('formulario_curso', formulario_curso, name='formulario_curso'),
    path('busqueda_curso', busqueda_curso, name='busqueda_curso')
]