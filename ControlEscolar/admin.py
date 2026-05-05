from django.contrib import admin
from .models import Licenciatura, Grupo, Semestre, PeriodoEscolar, AlumnoGrupo

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'abreviatura')
    search_fields = ('nombre', 'abreviatura')

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('idgrupo', 'nombre')
    search_fields = ('nombre',)

@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('idsemestre', 'numero')

@admin.register(PeriodoEscolar)
class PeriodoEscolarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')

@admin.register(AlumnoGrupo)
class AlumnoGrupoAdmin(admin.ModelAdmin):
    list_display = ('idalumno', 'idgrupo', 'idperiodo')
    list_filter = ('idgrupo', 'idperiodo')
    search_fields = ('idalumno__matricula',)