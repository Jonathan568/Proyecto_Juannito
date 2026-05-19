from django.contrib import admin
from .models import Libro, LibroFisico, Prestamo

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # Despliega los detalles principales del catálogo impreso
    list_display = ('idlibro', 'titulo', 'autor', 'isbn', 'editorial')
    # Permite buscar instantáneamente por título, isbn o autor
    search_fields = ('titulo', 'isbn', 'autor')
    ordering = ('titulo',)


@admin.register(LibroFisico)
class LibroFisicoAdmin(admin.ModelAdmin):
    # Muestra el código de barras único y el enlace al catálogo base
    list_display = ('idlibrofisico', 'codigo_barras', 'idlibro', 'estado')
    # Permite filtrar los libros físicos por su disponibilidad en el inventario
    list_filter = ('estado',)
    # Habilita la búsqueda cruzada: puedes buscar un ejemplar por su código o por el título del libro
    search_fields = ('codigo_barras', 'idlibro__titulo')
    # Optimiza el formulario vinculando el catálogo mediante ID interactivo
    raw_id_fields = ('idlibro',)


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    # Despliega el folio, el estudiante involucrado, el libro prestado y las fechas de control
    list_display = ('idprestamo', 'idalumno', 'idlibrofisico', 'fecha_salida', 'fecha_devolucion', 'estatus')
    # Segmenta la auditoría del administrador por estado del préstamo y rangos de fecha
    list_filter = ('estatus', 'fecha_salida', 'fecha_devolucion')
    # Búsqueda relacional profunda: encuentra un préstamo escribiendo la matrícula, nombre del alumno, código de barras o título del libro
    search_fields = (
        'idalumno__matricula', 
        'idalumno__nombre', 
        'idlibrofisico__codigo_barras', 
        'idlibrofisico__idlibro__titulo'
    )
    # Protege los selectores para evitar cargas lentas al buscar el alumno o el libro físico
    raw_id_fields = ('idalumno', 'idlibrofisico')
    # Ordena automáticamente poniendo los préstamos más recientes al principio
    ordering = ('-fecha_salida',)