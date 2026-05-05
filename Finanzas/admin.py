from django.contrib import admin
from .models import Concepto, Pago, CargoAlumno

@admin.register(Concepto)
class ConceptoAdmin(admin.ModelAdmin):
    list_display = ('idconcepto', 'nombre', 'precio')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('idpago', 'folio', 'monto', 'fecha', 'estatus')
    list_filter = ('estatus', 'fecha')
    search_fields = ('folio',)

@admin.register(CargoAlumno)
class CargoAlumnoAdmin(admin.ModelAdmin):
    list_display = ('idalumno', 'idconcepto', 'monto', 'estatus', 'fecha')
    list_filter = ('estatus',)
    search_fields = ('idalumno__matricula',)