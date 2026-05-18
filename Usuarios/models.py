from django.db import models

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=10)

    # Conservamos la integración con tu base de datos externa intacta
    class Meta:
        managed = False
        db_table = 'Usuario'
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
    estatus = models.CharField(max_length=10)
    idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idUsuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Alumno'
        verbose_name = "Estudiante"
        verbose_name_plural = "Catálogo de Estudiantes"

    # Desiega la matrícula con el nombre y apellido paterno completo del alumno
    def __str__(self):
        apellido_str = f" {self.apellido_paterno}" if self.apellido_paterno else ""
        return f"{self.matricula} — {self.nombre}{apellido_str}"