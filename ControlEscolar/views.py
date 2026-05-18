from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count

from .models import CicloEscolar, Asignatura, Grupo, AlumnoGrupo, Horario, Inscripcion, Aviso
from Usuarios.models import Alumno

@login_required
def dashboard_admin(request):
    """Vista principal del panel de Control Escolar para administradores"""
    if not request.user.is_staff and not request.user.is_superuser:
        messages.error(request, 'Acceso denegado: Área exclusiva de Control Escolar.')
        return redirect('Usuarios:panel_alumno')

    ciclo_actual = CicloEscolar.objects.filter(estatus='activo').first()

    total_alumnos = Alumno.objects.filter(estatus='activo').count()
    total_grupos = Grupo.objects.filter(idciclo=ciclo_actual).count() if ciclo_actual else 0
    total_materias = Asignatura.objects.count()

    avisos_recientes = Aviso.objects.order_by('-fecha_publicacion')[:5]

    # --- PROCESAMIENTO OPERACIONAL DE LICENCIATURAS REALES (Cupos Dinámicos) ---
    licenciaturas_vivas = []
    
    if ciclo_actual:
        # Consultamos las licenciaturas (Grupos) del ciclo activo y contamos sus alumnos inscritos en tiempo real
        grupos_db = Grupo.objects.filter(idciclo=ciclo_actual).annotate(
            total_inscritos=Count('alumnogrupo')
        ).order_by('-total_inscritos')
        
        for g in grupos_db:
            # Establecemos un límite óptimo de diseño de 50 alumnos por aula
            capacidad_maxima = 50
            porcentaje = int((g.total_inscritos / capacidad_maxima) * 100) if g.total_inscritos else 0
            if porcentaje > 100: 
                porcentaje = 100
            
            # Clasificación analítica automática según volumen poblacional en base de datos
            if g.total_inscritos >= 40:
                estatus_cupo = 'Límite'
                color_badge = 'bg-red-100 text-red-700'
                color_bar = 'bg-red-500'
            elif g.total_inscritos >= 15:
                estatus_cupo = 'Óptimo'
                color_badge = 'bg-emerald-100 text-emerald-700'
                color_bar = 'bg-blue-500'
            else:
                estatus_cupo = 'Baja'
                color_badge = 'bg-amber-100 text-amber-700'
                color_bar = 'bg-amber-500'
                
            # Asignación heurística de iconos según el nombre de la Licenciatura
            nombre_lower = g.nombre.lower()
            if 'computaci' in nombre_lower or 'sistemas' in nombre_lower or 'ing' in nombre_lower:
                icono = 'fas fa-laptop-code'
                color_icon = 'bg-blue-50 text-blue-600'
            elif 'derecho' in nombre_lower or 'ley' in nombre_lower or 'gavel' in nombre_lower:
                icono = 'fas fa-balance-scale'
                color_icon = 'bg-amber-50 text-amber-600'
            elif 'lengua' in nombre_lower or 'idioma' in nombre_lower or 'modernas' in nombre_lower:
                icono = 'fas fa-language'
                color_icon = 'bg-emerald-50 text-emerald-600'
            else:
                icono = 'fas fa-graduation-cap'
                color_icon = 'bg-indigo-50 text-indigo-600'

            licenciaturas_vivas.append({
                'nombre': g.nombre,
                'total_inscritos': g.total_inscritos,
                'porcentaje': porcentaje,
                'estatus_cupo': estatus_cupo,
                'color_badge': color_badge,
                'color_bar': color_bar,
                'icono': icono,
                'color_icon': color_icon
            })

    context = {
        'ciclo_actual': ciclo_actual,
        'total_alumnos': total_alumnos,
        'total_grupos': total_grupos,
        'total_materias': total_materias,
        'avisos_recientes': avisos_recientes,
        'licenciaturas_vivas': licenciaturas_vivas, # Pasamos la lista procesada al HTML
    }
    
    return render(request, 'controlescolar/admin/dashboard_admin.html', context)

@login_required
def gestionar_grupos(request):
    """Vista para listar grupos y buscar alumnos para moverlos"""
    if not request.user.is_staff:
        return redirect('Usuarios:panel_alumno')

    ciclo_actual = CicloEscolar.objects.filter(estatus='activo').first()
    grupos = Grupo.objects.filter(idciclo=ciclo_actual)
    
    q = request.GET.get('q', '')
    alumnos_asignados = AlumnoGrupo.objects.select_related('idalumno', 'idgrupo').filter(
        idgrupo__idciclo=ciclo_actual
    )

    if q:
        alumnos_asignados = alumnos_asignados.filter(
            Q(idalumno__nombre__icontains=q) | 
            Q(idalumno__matricula__icontains=q)
        )

    context = {
        'grupos': grupos,
        'alumnos_asignados': alumnos_asignados,
        'ciclo_actual': ciclo_actual,
        'q': q
    }
    return render(request, 'controlescolar/admin/gestionar_grupos.html', context)

@login_required
def mover_alumno_grupo(request):
    """Procesa el cambio de grupo de un alumno de forma blindada"""
    if request.method == 'POST' and request.user.is_staff:
        # Soportamos ambas nomenclaturas por seguridad total contra cambios en el HTML
        alumno_id = request.POST.get('idalumno') or request.POST.get('alumno_id')
        nuevo_grupo_id = request.POST.get('idgrupo') or request.POST.get('nuevo_grupo_id')
        
        asignacion = get_object_or_404(AlumnoGrupo, idalumno_id=alumno_id)
        nuevo_grupo = get_object_or_404(Grupo, id=nuevo_grupo_id)
        
        asignacion.idgrupo = nuevo_grupo
        asignacion.save()
        
        messages.success(request, f'Alumno movido a la licenciatura {nuevo_grupo.nombre} exitosamente.')
    
    return redirect('ControlEscolar:gestionar_grupos')

@login_required
def gestionar_horarios(request):
    """Vista para crear y ver la carga académica por grupo"""
    if not request.user.is_staff:
        return redirect('Usuarios:panel_alumno')

    ciclo_actual = CicloEscolar.objects.filter(estatus='activo').first()
    grupos = Grupo.objects.filter(idciclo=ciclo_actual)
    asignaturas = Asignatura.objects.all()

    grupo_seleccionado_id = request.GET.get('grupo_id')
    horarios = None
    grupo_seleccionado = None

    if grupo_seleccionado_id:
        grupo_seleccionado = get_object_or_404(Grupo, id=grupo_seleccionado_id)
        horarios = Horario.objects.filter(idgrupo=grupo_seleccionado).order_by('dia', 'hora_inicio')

    if request.method == 'POST':
        idgrupo = request.POST.get('idgrupo')
        grupo = get_object_or_404(Grupo, id=idgrupo)
        asignatura = get_object_or_404(Asignatura, id=request.POST.get('idasignatura'))

        Horario.objects.create(
            idgrupo=grupo,
            idasignatura=asignatura,
            profesor_asignado=request.POST.get('profesor'),
            aula=request.POST.get('aula'),
            dia=request.POST.get('dia'),
            hora_inicio=request.POST.get('hora_inicio'),
            hora_fin=request.POST.get('hora_fin')
        )
        messages.success(request, 'Horario asignado correctamente.')
        return redirect(f"{request.path}?grupo_id={idgrupo}")

    context = {
        'grupos': grupos,
        'asignaturas': asignaturas,
        'horarios': horarios,
        'grupo_seleccionado': grupo_seleccionado,
        'dias_semana': Horario.DIAS_SEMANA
    }
    return render(request, 'controlescolar/admin/gestionar_horarios.html', context)

@login_required
def eliminar_horario(request, horario_id):
    """Elimina una clase asignada al horario"""
    if request.user.is_staff:
        horario = get_object_or_404(Horario, id=horario_id)
        grupo_id = horario.idgrupo.id
        horario.delete()
        messages.success(request, 'Horario eliminado exitosamente.')
        return redirect(f"/controlescolar/admin/horarios/?grupo_id={grupo_id}")
    return redirect('Usuarios:panel_alumno')

@login_required
def gestionar_avisos(request):
    """Vista para redactar y enviar avisos globales, grupales o individuales Bimorfos"""
    if not request.user.is_staff:
        return redirect('Usuarios:panel_alumno')

    avisos = Aviso.objects.all().order_by('-fecha_publicacion')
    grupos = Grupo.objects.all()
    alumnos = Alumno.objects.filter(estatus='activo')

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        aviso = Aviso(
            titulo=request.POST.get('titulo'),
            mensaje=request.POST.get('mensaje'),
            tipo=tipo
        )
        
        if tipo == 'grupal':
            aviso.idgrupo = get_object_or_404(Grupo, id=request.POST.get('idgrupo'))
        elif tipo == 'individual':
            aviso.idalumno = get_object_or_404(Alumno, id=request.POST.get('idalumno'))
            
        aviso.save()
        messages.success(request, 'Aviso publicado correctamente.')
        return redirect('ControlEscolar:gestionar_avisos')

    context = {
        'avisos': avisos,
        'grupos': grupos,
        'alumnos': alumnos,
    }
    return render(request, 'controlescolar/admin/gestionar_avisos.html', context)

@login_required
def eliminar_aviso(request, aviso_id):
    """Elimina un aviso del muro"""
    if request.user.is_staff:
        aviso = get_object_or_404(Aviso, id=aviso_id)
        aviso.delete()
        messages.success(request, 'Aviso eliminado.')
    return redirect('ControlEscolar:gestionar_avisos')

@login_required
def dashboard_alumno(request):
    """Vista del panel de Control Escolar exclusivo para el estudiante"""
    alumno = Alumno.objects.filter(idusuario_id=request.user.id).first()
    
    if not alumno:
        messages.error(request, 'No tienes un perfil de estudiante asignado.')
        return redirect('inicio')

    ciclo_actual = CicloEscolar.objects.filter(estatus='activo').first()
    asignacion = AlumnoGrupo.objects.filter(idalumno=alumno).first()
    grupo_actual = asignacion.idgrupo if asignacion else None

    horarios = None
    if grupo_actual:
        horarios = Horario.objects.filter(idgrupo=grupo_actual).order_by('dia', 'hora_inicio')

    avisos = Aviso.objects.filter(
        Q(tipo='global') | 
        Q(tipo='grupal', idgrupo=grupo_actual) | 
        Q(tipo='individual', idalumno=alumno)
    ).order_by('-fecha_publicacion')

    context = {
        'alumno': alumno,
        'grupo_actual': grupo_actual,
        'ciclo_actual': ciclo_actual,
        'horarios': horarios,
        'avisos': avisos,
    }
    
    return render(request, 'controlescolar/alumno/dashboard_alumno.html', context)

@login_required
def gestionar_calificaciones(request):
    """Vista del administrador para asentar calificaciones por grupo y materia"""
    if not request.user.is_staff:
        return redirect('Usuarios:panel_alumno')

    ciclo_actual = CicloEscolar.objects.filter(estatus='activo').first()
    grupos = Grupo.objects.filter(idciclo=ciclo_actual)

    grupo_id = request.GET.get('grupo_id')
    asignatura_id = request.GET.get('asignatura_id')

    grupo_seleccionado = None
    asignatura_seleccionada = None
    asignaturas_grupo = []
    inscripciones = []

    if grupo_id:
        grupo_seleccionado = get_object_or_404(Grupo, id=grupo_id)
        asignaturas_grupo = Asignatura.objects.filter(horario__idgrupo=grupo_seleccionado).distinct()

    if grupo_seleccionado and asignatura_id:
        asignatura_seleccionada = get_object_or_404(Asignatura, id=asignatura_id)
        alumnos_grupo = AlumnoGrupo.objects.filter(idgrupo=grupo_seleccionado)

        for ag in alumnos_grupo:
            inscripcion, created = Inscripcion.objects.get_or_create(
                idalumno=ag.idalumno,
                idasignatura=asignatura_seleccionada,
                idciclo=ciclo_actual,
                defaults={'estatus': 'cursando'}
            )
            inscripciones.append(inscripcion)

    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('calif_'):
                insc_id = key.split('_')[1]
                insc = get_object_or_404(Inscripcion, id=insc_id)

                calif_val = value if value.strip() != "" else None
                estatus_val = request.POST.get(f'estatus_{insc_id}')
                
                insc.calificacion_final = calif_val
                insc.estatus = estatus_val
                insc.save()
        
        messages.success(request, 'Calificaciones guardadas exitosamente.')
        return redirect(f"{request.path}?grupo_id={grupo_seleccionado.id}&asignatura_id={asignatura_seleccionada.id}")

    context = {
        'grupos': grupos,
        'grupo_seleccionado': grupo_seleccionado,
        'asignaturas_grupo': asignaturas_grupo,
        'asignatura_seleccionada': asignatura_seleccionada,
        'inscripciones': inscripciones,
        'ciclo_actual': ciclo_actual
    }
    return render(request, 'controlescolar/admin/gestionar_calificaciones.html', context)


@login_required
def boleta_alumno(request):
    """Vista para que el alumno vea su historial o Kárdex"""
    alumno = Alumno.objects.filter(idusuario_id=request.user.id).first()
    
    if not alumno:
        return redirect('inicio')

    inscripciones = Inscripcion.objects.filter(idalumno=alumno).order_by('-idciclo__fecha_inicio', 'idasignatura__nombre')

    calificaciones_validas = [i.calificacion_final for i in inscripciones if i.calificacion_final is not None]
    promedio = sum(calificaciones_validas) / len(calificaciones_validas) if calificaciones_validas else 0

    context = {
        'alumno': alumno,
        'inscripciones': inscripciones,
        'promedio': round(promedio, 2)
    }
    return render(request, 'controlescolar/alumno/boleta_alumno.html', context)