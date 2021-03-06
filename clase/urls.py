from django.urls import path
# from .views import formulario_curso, nuevo_curso, busqueda_curso, crear_estudiante, estudiante, borrar_estudiante, actualizar_estudiante, listado_estudiantes
from . import views

urlpatterns = [
    path('nuevo/', views.nuevo_curso, name='nuevo_curso'),
    path('formulario_curso', views.formulario_curso, name='formulario_curso'),
    path('busqueda_curso', views.busqueda_curso, name='busqueda_curso'),

    # path('estudiante/', estudiante, name='estudiante'),
    path('estudiante/listado_estudiantes', views.listado_estudiantes, name='listado_estudiantes'),
    path('estudiante/crear_estudiante', views.crear_estudiante, name='crear_estudiante'),
    path('estudiante/borrar/<int:id>', views.borrar_estudiante, name='borrar_estudiante'),
    path('estudiante/actualizar/<int:id>', views.actualizar_estudiante, name='actualizar_estudiante'),

    path('profesores', views.ProfesorLista.as_view(), name="profesor_listado"),
    path('profesores/<int:pk>', views.ProfesorDetalle.as_view(), name="profesor_detalle"),
    path('profesores/<int:pk>/editar', views.ProfesorEditar.as_view(), name="profesor_editar"),
    path('profesores/<int:pk>/borrar', views.ProfesorBorrar.as_view(), name="profesor_borrar")
]