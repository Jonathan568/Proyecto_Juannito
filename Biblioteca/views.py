from django.shortcuts import render
from .models import Libro
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

@login_required
def dashboard_admin(request):
    return render(request, 'biblioteca/admin/dashboard_admin_biblioteca.html')

@login_required
def dashboard_alumno(request):
    return render(request, 'biblioteca/alumno/dashboard_alumno_biblioteca.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Libro, LibroFisico, Prestamo
from Usuarios.models import Alumno

@login_required
def gestion_biblioteca(request):
    """Vista para que el Admin vea todos los libros y su estado actual"""

    if not request.user.is_staff:
        return redirect('Usuarios:login')

    inventario = LibroFisico.objects.select_related('idlibro').all()

    return render(request, 'biblioteca/admin/gestion_biblioteca.html', {
        'inventario': inventario
    })

@login_required
def catalogo_alumno(request):
    """Vista para que el Alumno vea libros disponibles"""
    libros_disponibles = LibroFisico.objects.filter(estado='disponible').select_related('idlibro')
    
    return render(request, 'biblioteca/alumno/catalogo_alumno.html', {
        'libros': libros_disponibles
    })

@login_required
def solicitar_prestamo(request, libro_id):
    """Procesa la solicitud de un libro por parte de un alumno"""

    libro_fisico = get_object_or_404(LibroFisico, idlibrofisico=libro_id)

    alumno = Alumno.objects.filter(idusuario_id=request.user.id).first()
    
    if not alumno:
        messages.error(request, 'No tienes un perfil de estudiante para solicitar libros.')
        return redirect('Biblioteca:catalogo_alumno')
 
    if libro_fisico.estado != 'disponible':
        messages.error(request, 'Lo sentimos, este libro acaba de ser prestado.')
        return redirect('Biblioteca:catalogo_alumno')

    Prestamo.objects.create(
        idalumno=alumno,
        idlibrofisico=libro_fisico,
        fecha_salida=timezone.now(),
        estatus='activo'
    )

    libro_fisico.estado = 'prestado'
    libro_fisico.save()

    messages.success(request, f'¡Has solicitado "{libro_fisico.idlibro.titulo}" con éxito! Pasa a recogerlo a biblioteca.')
    return redirect('Biblioteca:catalogo_alumno')

@login_required
def registrar_libro(request):
    """Procesa el formulario para agregar un nuevo libro al inventario"""
    if request.method == 'POST' and request.user.is_staff:

        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        isbn = request.POST.get('isbn')
        editorial = request.POST.get('editorial')
        codigo_barras = request.POST.get('codigo_barras')

        nuevo_libro = Libro.objects.create(
            titulo=titulo,
            autor=autor,
            isbn=isbn,
            editorial=editorial
        )

        LibroFisico.objects.create(
            codigo_barras=codigo_barras,
            estado='disponible',
            idlibro=nuevo_libro
        )
        
        messages.success(request, f'El libro "{titulo}" se ha registrado exitosamente.')
    
    return redirect('Biblioteca:gestion_biblioteca')

from django.utils import timezone

@login_required
def devolver_libro(request, libro_fisico_id):
    """Procesa la devolución de un libro: lo pone disponible y cierra el préstamo"""
    if request.user.is_staff:
        libro_fisico = get_object_or_404(LibroFisico, idlibrofisico=libro_fisico_id)
        prestamo = Prestamo.objects.filter(idlibrofisico=libro_fisico, estatus='activo').last()
        
        if prestamo:
            prestamo.fecha_devolucion = timezone.now()
            prestamo.estatus = 'devuelto'
            prestamo.save()
        libro_fisico.estado = 'disponible'
        libro_fisico.save()
        
        messages.success(request, f'El libro "{libro_fisico.idlibro.titulo}" ha sido devuelto y ya está disponible.')
    
    return redirect('Biblioteca:gestion_biblioteca')

@login_required
def eliminar_libro(request, libro_fisico_id):
    """Elimina un ejemplar físico del inventario"""
    if request.user.is_staff:
        libro_fisico = get_object_or_404(LibroFisico, idlibrofisico=libro_fisico_id)
        titulo = libro_fisico.idlibro.titulo
        libro_fisico.delete()
        messages.warning(request, f'Se ha eliminado el ejemplar de "{titulo}" del inventario.')
        
    return redirect('Biblioteca:gestion_biblioteca')

@login_required
def catalogo_alumno(request):
    """Vista para que el Alumno vea libros disponibles con buscador"""

    q = request.GET.get('q', '')
    
    libros = LibroFisico.objects.filter(estado='disponible').select_related('idlibro')
    
    if q:
        libros = libros.filter(
            Q(idlibro__titulo__icontains=q) | 
            Q(idlibro__autor__icontains=q)
        )
        
    return render(request, 'biblioteca/alumno/catalogo_alumno.html', {
        'libros': libros,
        'q': q 
    })
