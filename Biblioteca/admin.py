from django.contrib import admin
from .models import Libro, LibroFisico, Prestamo

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'editorial')
    search_fields = ('titulo', 'isbn', 'autor')

@admin.register(LibroFisico)
class LibroFisicoAdmin(admin.ModelAdmin):
    list_display = ('codigo_barras', 'idlibro', 'estado')
    list_filter = ('estado',)

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('idalumno', 'idlibrofisico', 'fecha_salida', 'estatus')
    list_filter = ('estatus', 'fecha_salida')