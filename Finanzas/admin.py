from django.contrib import admin
from .models import Concepto, Pago, CargoAlumno

@admin.register(Concepto)
class ConceptoAdmin(admin.ModelAdmin):
    # Despliega los detalles del catálogo de cobros institucionales
    list_display = ('idconcepto', 'nombre', 'precio')
    # Permite buscar rápidamente conceptos por su nombre
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    # Despliega la información de las transacciones y recibos validados
    list_display = ('idpago', 'folio', 'monto', 'fecha', 'estatus')
    # Permite auditar ingresos por estado de la transacción y rangos de fecha
    list_filter = ('estatus', 'fecha')
    # Buscador directo por el número de folio o ID del recibo
    search_fields = ('folio', 'idpago')
    ordering = ('-fecha',)


@admin.register(CargoAlumno)
class CargoAlumnoAdmin(admin.ModelAdmin):
    # Despliega el desglose del estado de cuenta de cada estudiante
    list_display = ('idcargo', 'idalumno', 'idconcepto', 'monto', 'estatus', 'fecha', 'idpago')
    # Segmenta la lista por el estado del cargo (pendiente, pagado, cancelado) y su fecha de emisión
    list_filter = ('estatus', 'fecha')
    # Búsqueda relacional profunda: localiza cargos por matrícula, nombre del alumno o concepto arancelario
    search_fields = (
        'idalumno__matricula', 
        'idalumno__nombre', 
        'idconcepto__nombre'
    )
    # Optimiza y blinda los selectores del formulario para evitar listas masivas lentas
    raw_id_fields = ('idalumno', 'idconcepto', 'idpago')
    # Ordena mostrando los cargos más recientes en la parte superior
    ordering = ('-fecha',)