from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from django.contrib import messages
from django.utils import timezone

from .models import CargoAlumno, Concepto

# Modelos de tus otras aplicaciones (Asegúrate de que los nombres de las apps y modelos coincidan)
from Usuarios.models import Alumno
from ControlEscolar.models import Grupo, AlumnoGrupo


@login_required
def dashboard_admin(request):
    """Vista principal del administrador financiero"""
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
    """Vista principal del estado de cuenta del alumno"""

    alumno = Alumno.objects.filter(idusuario=request.user.id).first()

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


@login_required
def nuevo_cargo(request):
    """Vista para asignar cargos individuales o masivos (grupales) y crear conceptos dinámicos"""
    if request.method == 'POST':
        tipo_cargo = request.POST.get('tipo_cargo')
        concepto_input = request.POST.get('concepto')
        monto = request.POST.get('monto')
        fecha = request.POST.get('fecha')

        if float(monto) <= 0:
            messages.error(request, 'El monto del cargo debe ser mayor a $0.00.')
            return redirect('Finanzas:nuevo_cargo')
        
        try:

            try:
  
                concepto_obj = Concepto.objects.get(idconcepto=int(concepto_input))
            except (ValueError, TypeError, Concepto.DoesNotExist):

                concepto_obj, created = Concepto.objects.get_or_create(
                    nombre=concepto_input.strip(),
                    defaults={'precio': monto}
                )

            if tipo_cargo == 'individual':
                idalumno_id = request.POST.get('alumno')
                
                CargoAlumno.objects.create(
                    idalumno_id=idalumno_id, 
                    idconcepto=concepto_obj,
                    monto=monto,
                    fecha=fecha,
                    estatus='pendiente'
                )
                messages.success(request, 'Cargo individual asignado correctamente.')

            elif tipo_cargo == 'grupal':
                idgrupo_id = request.POST.get('grupo')
                
                alumnos_del_grupo = AlumnoGrupo.objects.filter(idgrupo_id=idgrupo_id)
                
                if not alumnos_del_grupo.exists():
                    messages.warning(request, 'Atención: El grupo seleccionado no tiene alumnos inscritos.')
                    return redirect('Finanzas:nuevo_cargo')

                for registro in alumnos_del_grupo:
                    CargoAlumno.objects.create(
                        idalumno_id=registro.idalumno_id,
                        idconcepto=concepto_obj,
                        monto=monto,
                        fecha=fecha,
                        estatus='pendiente'
                    )
                messages.success(request, f'Cargos grupales asignados a {alumnos_del_grupo.count()} alumnos.')
                
            return redirect('Finanzas:dashboard_admin')
            
        except Exception as e:
            messages.error(request, f'Error al procesar el cargo: {str(e)}')
            return redirect('Finanzas:nuevo_cargo')

    conceptos = Concepto.objects.all()
    alumnos = Alumno.objects.filter(estatus='activo')
    grupos = Grupo.objects.all()
    
    context = {
        'conceptos': conceptos,
        'alumnos': alumnos,
        'grupos': grupos,
    }
    return render(request, 'finanzas/admin/nuevo_cargo.html', context)


@login_required
def historial_cargos(request):
    """Vista para consultar y filtrar todos los registros financieros"""
    q_alumno = request.GET.get('alumno', '')
    q_concepto = request.GET.get('concepto', '')
    q_estado = request.GET.get('estado', '')

    cargos = CargoAlumno.objects.select_related('idalumno', 'idconcepto').all().order_by('-fecha')

    if q_alumno:
        cargos = cargos.filter(
            Q(idalumno__nombre__icontains=q_alumno) | 
            Q(idalumno__apellido_paterno__icontains=q_alumno) |
            Q(idalumno__matricula__icontains=q_alumno)
        )
    
    if q_concepto:
        cargos = cargos.filter(idconcepto__idconcepto=q_concepto)
        
    if q_estado:
        cargos = cargos.filter(estatus=q_estado)

    conceptos = Concepto.objects.all()

    context = {
        'cargos': cargos,
        'conceptos': conceptos,
        'q_alumno': q_alumno,
        'q_concepto': q_concepto,
        'q_estado': q_estado,
    }
    return render(request, 'finanzas/admin/historial_cargos.html', context)


@login_required
def generar_ficha(request):
    """Vista para procesar los cargos seleccionados y generar el documento de pago"""
    if request.method == 'POST':
        cargos_ids = request.POST.getlist('cargos_seleccionados')
        
        if not cargos_ids:
            messages.error(request, 'Debes seleccionar al menos un cargo para generar la ficha.')
            return redirect('Finanzas:dashboard_alumno')
            
        cargos_a_pagar = CargoAlumno.objects.filter(idcargo__in=cargos_ids).select_related('idconcepto')
        total_ficha = cargos_a_pagar.aggregate(Sum('monto'))['monto__sum'] or 0.00

        alumno_actual = Alumno.objects.filter(idusuario=request.user.id).first()
        
        context = {
            'cargos': cargos_a_pagar,
            'total_ficha': total_ficha,
            'fecha_impresion': timezone.now(),
            'alumno': alumno_actual
        }
        
        return render(request, 'finanzas/alumno/ficha_pago.html', context)
        
    return redirect('Finanzas:dashboard_alumno')