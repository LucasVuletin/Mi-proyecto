from django.contrib import admin

from clase.models import curso

# Register your models here.

from .models import curso, profesor, entregable, estudiante

admin.site.register(curso)
admin.site.register(profesor)
admin.site.register(entregable)
admin.site.register(estudiante)
