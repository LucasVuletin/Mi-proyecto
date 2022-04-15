from django.urls import path
from .views import formulario_curso, nuevo_curso
urlpatterns = [
    path('nuevo/', nuevo_curso, name='nuevo_curso'),
    path('', formulario_curso, name='formulario_curso')
]