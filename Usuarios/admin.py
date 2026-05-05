from django.contrib import admin
from .models import Usuario, Alumno

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('idusuario', 'username', 'rol')
    search_fields = ('username',)
    list_filter = ('rol',)

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nombre', 'apellido_paterno', 'estatus')
    search_fields = ('matricula', 'nombre', 'apellido_paterno')
    list_filter = ('estatus',)