from django.contrib import admin
from .models import CicloEscolar, Asignatura, Grupo, AlumnoGrupo, Horario, Inscripcion, Aviso

# Registramos los nuevos modelos en el panel de administrador
admin.site.register(CicloEscolar)
admin.site.register(Asignatura)
admin.site.register(Grupo)
admin.site.register(AlumnoGrupo)
admin.site.register(Horario)
admin.site.register(Inscripcion)
admin.site.register(Aviso)