from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Usuarios.models import Alumno

class Libro(models.Model):
    idlibro = models.AutoField(db_column='idLibro', primary_key=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    autor = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    editorial = models.CharField(max_length=100, blank=True, null=True)

    # Conservamos intactos tus parámetros db_table y managed para no romper la BD
    class Meta:
        managed = False
        db_table = 'libro'
        verbose_name = "Libro (Título)"
        verbose_name_plural = "Catálogo de Libros"

    # Representación limpia en los selectores y listas del admin
    def __str__(self):
        return f"{self.titulo} — {self.autor}" if self.titulo else f"Libro #{self.idlibro}"


class LibroFisico(models.Model):
    idlibrofisico = models.AutoField(db_column='idLibroFisico', primary_key=True)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True) # ENUM
    idlibro = models.ForeignKey(Libro, models.PROTECT, db_column='idLibro') # PROTECT es más seguro

    class Meta:
        managed = False
        db_table = 'libro_fisico'
        verbose_name = "Ejemplar Físico"
        verbose_name_plural = "Inventario de Ejemplares Físicos"

    # Enlaza visualmente el código de barras con el título del catálogo
    def __str__(self):
        titulo_libro = self.idlibro.titulo if self.idlibro else "Desconocido"
        return f"[{self.codigo_barras}] {titulo_libro}"


class Prestamo(models.Model):
    idprestamo = models.AutoField(db_column='idPrestamo', primary_key=True)
    idalumno = models.ForeignKey('Usuarios.Alumno', models.PROTECT, db_column='idAlumno')
    idlibrofisico = models.ForeignKey(LibroFisico, models.PROTECT, db_column='idLibroFisico')
    fecha_salida = models.DateTimeField(blank=True, null=True)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=10, blank=True, null=True) # ENUM

    class Meta:
        managed = False
        db_table = 'prestamo'
        verbose_name = "Préstamo de Libro"
        verbose_name_plural = "Control de Préstamos"

    # Muestra un resumen directo de a quién se le prestó y qué libro es
    def __str__(self):
        try:
            titulo = self.idlibrofisico.idlibro.titulo
            matricula = self.idalumno.matricula
            return f"Folio {self.idprestamo} — {titulo} ({matricula})"
        except AttributeError:
            return f"Préstamo Folio #{self.idprestamo}"