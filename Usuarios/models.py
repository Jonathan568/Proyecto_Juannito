from django.db import models

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=15, default='alumno')  # Ampliado por seguridad contra truncados

    class Meta:
        managed = True  # ¡Salto de control activo!
        db_table = 'usuario'  # Mapeado de forma unificada en minúsculas
        verbose_name = "Usuario"
        verbose_name_plural = "Credenciales de Usuarios"

    # Muestra el nombre de usuario junto con su rol en mayúsculas para mejor control
    def __str__(self):
        rol_str = self.rol.upper() if self.rol else "SIN ROL"
        return f"{self.username} [{rol_str}]"


class Alumno(models.Model):
    idalumno = models.AutoField(db_column='idAlumno', primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido_paterno = models.CharField(max_length=45)
    matricula = models.CharField(unique=True, max_length=45)
    estatus = models.CharField(max_length=20, default='activo')  # Ampliado a 20 para evitar truncados
    
    # Reemplazado DO_NOTHING por SET_NULL para blindar la consistencia de datos escolares
    idusuario = models.ForeignKey('Usuario', models.SET_NULL, db_column='idUsuario', blank=True, null=True)

    class Meta:
        managed = True  # ¡Salto de control activo!
        db_table = 'alumno'  # Mapeado de forma unificada en minúsculas
        verbose_name = "Estudiante"
        verbose_name_plural = "Catálogo de Estudiantes"

    # Despliega la matrícula con el nombre y apellido paterno completo del alumno
    def __str__(self):
        apellido_str = f" {self.apellido_paterno}" if self.apellido_paterno else ""
        return f"{self.matricula} — {self.nombre}{apellido_str}"