from django.db import models

class Libro(models.Model):
    idlibro = models.AutoField(db_column='idLibro', primary_key=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    autor = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    editorial = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Libro'

class LibroFisico(models.Model):
    idlibrofisico = models.AutoField(db_column='idLibroFisico', primary_key=True)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    idlibro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='idLibro')

    class Meta:
        managed = False
        db_table = 'Libro_Fisico'

class Prestamo(models.Model):
    idprestamo = models.AutoField(db_column='idPrestamo', primary_key=True)
    idalumno = models.ForeignKey('Usuarios.Alumno', models.DO_NOTHING, db_column='idAlumno')
    idlibrofisico = models.ForeignKey(LibroFisico, models.DO_NOTHING, db_column='idLibroFisico')
    fecha_salida = models.DateTimeField(blank=True, null=True)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Prestamo'