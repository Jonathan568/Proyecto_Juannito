from django.db import models

class Licenciatura(models.Model):
    idlicenciatura = models.AutoField(db_column='idLicenciatura', primary_key=True)
    nombre = models.CharField(max_length=45)
    abreviatura = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Licenciatura'

    def __str__(self):
        return f"{self.abreviatura} - {self.nombre}"

class Grupo(models.Model):
    idgrupo = models.AutoField(db_column='idGrupo', primary_key=True)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Grupo'

    def __str__(self):
        return self.nombre

class Semestre(models.Model):
    idsemestre = models.AutoField(db_column='idSemestre', primary_key=True)
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Semestre'

    def __str__(self):
        return f"Semestre {self.numero}"

class PeriodoEscolar(models.Model):
    idperiodo = models.AutoField(db_column='idPeriodo', primary_key=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Periodo_Escolar'

    def __str__(self):
        return self.nombre if self.nombre else f"Periodo {self.idperiodo}"

# Tabla de relación Histórica
class AlumnoGrupo(models.Model):
    # Referencia a la nueva carpeta 'Usuarios'
    idalumno = models.OneToOneField('Usuarios.Alumno', models.DO_NOTHING, db_column='idAlumno', primary_key=True)
    idgrupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='idGrupo')
    idperiodo = models.ForeignKey('PeriodoEscolar', models.DO_NOTHING, db_column='idPeriodo')

    class Meta:
        managed = False
        db_table = 'Alumno_Grupo'
        unique_together = (('idalumno', 'idgrupo', 'idperiodo'),)

    def __str__(self):
        return f"{self.idalumno} en {self.idgrupo}"