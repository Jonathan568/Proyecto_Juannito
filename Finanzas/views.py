from django.shortcuts import render
from .models import Pago
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import CargoAlumno

def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'finanzas/lista.html', {'pagos': pagos})

@login_required
def dashboard_admin(request):
    total_recaudado = CargoAlumno.objects.filter(estatus='pagado').aggregate(Sum('monto'))['monto__sum'] or 0.00
    pendientes_conteo = CargoAlumno.objects.filter(estatus='pendiente').count()
    alertas_criticas = CargoAlumno.objects.filter(estatus='pendiente', monto__gt=1000).count()

    pagos_recientes = CargoAlumno.objects.select_related('idalumno', 'idconcepto').order_by('-fecha')[:10]

    context = {
        'total_recaudado': total_recaudado,
        'pendientes_conteo': pendientes_conteo,
        'alertas_criticas': alertas_criticas,
        'pagos_recientes': pagos_recientes,
    }
    return render(request, 'finanzas/admin/dashboard_admin_finanzas.html', context)

@login_required
def dashboard_alumno(request):

    try:
        alumno = request.user.alumno_set.first() 
    except AttributeError:
        alumno = None

    if alumno:
        cargos_alumno = CargoAlumno.objects.filter(idalumno=alumno).select_related('idconcepto').order_by('-fecha')
        deuda_total = cargos_alumno.filter(estatus='pendiente').aggregate(Sum('monto'))['monto__sum'] or 0.00
    else:
        cargos_alumno = []
        deuda_total = 0.00

    context = {
        'cargos_alumno': cargos_alumno,
        'deuda_total': deuda_total,
    }
    return render(request, 'finanzas/alumno/dashboard_alumno_finanzas.html', context)