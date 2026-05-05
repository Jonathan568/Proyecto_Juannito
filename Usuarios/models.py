from django.db import models

class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Usuario'

    def __str__(self):
        return self.username

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

    def __str__(self):
        return f"{self.matricula} - {self.nombre}"