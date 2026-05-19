from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Usuarios.models import Alumno

class Libro(models.Model):
    idlibro = models.AutoField(db_column='idLibro', primary_key=True)
    titulo = models.CharField(max_length=100, blank=True, null=True)
    autor = models.CharField(max_length=100, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    editorial = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True  # ¡Salto de control activo!
        db_table = 'libro'
        verbose_name = "Libro (Título)"
        verbose_name_plural = "Catálogo de Libros"

    # Representación limpia en los selectores y listas del admin
    def __str__(self):
        return f"{self.titulo} — {self.autor}" if self.titulo else f"Libro #{self.idlibro}"


class LibroFisico(models.Model):
    idlibrofisico = models.AutoField(db_column='idLibroFisico', primary_key=True)
    codigo_barras = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=15, default='disponible') # Modificado a 15 caracteres con valor por defecto
    idlibro = models.ForeignKey(Libro, models.CASCADE, db_column='idLibro') # Ahora se borra si se elimina el catálogo base

    class Meta:
        managed = True  # ¡Salto de control activo!
        db_table = 'libro_fisico'
        verbose_name = "Ejemplar Físico"
        verbose_name_plural = "Inventario de Ejemplares Físicos"

    # Enlaza visualmente el código de barras con el título del catálogo
    def __str__(self):
        titulo_libro = self.idlibro.titulo if self.idlibro else "Desconocido"
        return f"[{self.codigo_barras}] {titulo_libro}"


class Prestamo(models.Model):
    idprestamo = models.AutoField(db_column='idPrestamo', primary_key=True)
    idalumno = models.ForeignKey('Usuarios.Alumno', models.CASCADE, db_column='idAlumno') # Si se borra el alumno, se borra su historial de préstamos
    idlibrofisico = models.ForeignKey(LibroFisico, models.PROTECT, db_column='idLibroFisico') # Evita borrar un libro físico si aún hay un préstamo activo
    fecha_salida = models.DateTimeField(blank=True, null=True)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    estatus = models.CharField(max_length=15, default='activo') # Modificado a 15 caracteres con valor por defecto

    class Meta:
        managed = True  # ¡Salto de control activo!
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