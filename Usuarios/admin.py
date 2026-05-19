from django.contrib import admin
from .models import Usuario, Alumno

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # Despliega los datos esenciales de las credenciales de acceso
    list_display = ('idusuario', 'username', 'rol')
    # Buscador rápido por nombre de usuario institucional
    search_fields = ('username',)
    # Filtro lateral para separar administradores de alumnos rápidamente
    list_filter = ('rol',)
    ordering = ('username',)


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    # Despliega el expediente principal del estudiante junto a su cuenta vinculada
    list_display = ('idalumno', 'matricula', 'nombre', 'apellido_paterno', 'estatus', 'idusuario')
    # Filtro de auditoría para identificar alumnos activos o inactivos
    list_filter = ('estatus',)
    # Búsqueda avanzada cruzada: busca por matrícula, nombre o incluso el username de su cuenta
    search_fields = (
        'matricula', 
        'nombre', 
        'apellido_paterno', 
        'idusuario__username'
    )
    # Selector blindado interactivo para vincular la cuenta de usuario sin que el panel se congele si hay miles de registros
    raw_id_fields = ('idusuario',)
    # Ordena alfabéticamente o por número de matrícula de forma automática
    ordering = ('matricula',)