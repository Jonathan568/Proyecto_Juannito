from django.contrib import admin
from .models import CicloEscolar, Asignatura, Grupo, AlumnoGrupo, Horario, Inscripcion, Aviso

@admin.register(CicloEscolar)
class CicloEscolarAdmin(admin.ModelAdmin):
    # Despliega los datos fundamentales del periodo
    list_display = ('id', 'nombre', 'fecha_inicio', 'fecha_fin', 'estatus')
    # Filtro rápido para ubicar periodos activos o históricos
    list_filter = ('estatus',)
    # Permite buscar directamente por la nomenclatura del ciclo
    search_fields = ('nombre',)


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    # Despliega los atributos del plan de estudios unificado
    list_display = ('id', 'clave', 'nombre', 'creditos', 'semestre_ideal', 'prerrequisito')
    # Permite filtrar las materias por el semestre sugerido
    list_filter = ('semestre_ideal',)
    # Buscador por clave institucional o nombre de la materia
    search_fields = ('clave', 'nombre')
    # Evita desplegar menús masivos si el catálogo crece
    raw_id_fields = ('prerrequisito',)


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    # Enmascarado visual del grupo como Licenciatura en la lista del panel
    list_display = ('id', 'nombre', 'semestre', 'idciclo')
    # Agrupa las licenciaturas por su ciclo escolar activo
    list_filter = ('idciclo', 'semestre')
    # Permite buscar programas específicos por nombre
    search_fields = ('nombre',)


@admin.register(AlumnoGrupo)
class AlumnoGrupoAdmin(admin.ModelAdmin):
    # Control de movimientos de matrícula escolar
    list_display = ('id', 'idalumno', 'idgrupo', 'fecha_asignacion')
    # Búsqueda cruzada: encuentra asignaciones por matrícula, nombre del estudiante o carrera
    search_fields = ('idalumno__matricula', 'idalumno__nombre', 'idgrupo__nombre')
    # Panel interactivo simplificado mediante ID relacional
    raw_id_fields = ('idalumno', 'idgrupo')


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    # Despliega la distribución de la carga académica áulica
    list_display = ('id', 'idgrupo', 'idasignatura', 'profesor_asignado', 'aula', 'dia', 'hora_inicio', 'hora_fin')
    # Filtros laterales por día de la semana y aulas
    list_filter = ('dia', 'aula')
    # Buscador por nombre de profesor, asignatura o carrera
    search_fields = ('profesor_asignado', 'idasignatura__nombre', 'idgrupo__nombre')
    # Vinculación relacional limpia
    raw_id_fields = ('idgrupo', 'idasignatura')


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    # Control analítico de actas y calificaciones finales
    list_display = ('id', 'idalumno', 'idasignatura', 'idciclo', 'estatus', 'calificacion_final')
    # Filtros clave por estatus académico (cursando, aprobada, reprobada) y ciclos
    list_filter = ('estatus', 'idciclo')
    # Búsqueda relacional profunda para auditorías de notas
    search_fields = ('idalumno__matricula', 'idalumno__nombre', 'idasignatura__nombre')
    # Blindaje relacional para selectores de actas
    raw_id_fields = ('idalumno', 'idasignatura', 'idciclo')


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    # Muro institucional de comunicados bimorfos
    list_display = ('id', 'titulo', 'tipo', 'idgrupo', 'idalumno', 'fecha_publicacion')
    # Segmentación por tipo de aviso (global, grupal, individual)
    list_filter = ('tipo', 'fecha_publicacion')
    # Permite buscar palabras clave dentro del título o contenido del mensaje
    search_fields = ('titulo', 'mensaje', 'idalumno__matricula', 'idgrupo__nombre')
    # Selectores opcionales controlados
    raw_id_fields = ('idgrupo', 'idalumno')