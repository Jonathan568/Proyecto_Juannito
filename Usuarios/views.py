from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Alumno


def registro(request):
    """
    Maneja la creación de nuevos usuarios usando el formulario seguro de Django.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Bienvenido {username}! Tu cuenta ha sido creada exitosamente.')
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    return render(request, 'Usuarios/registro.html', {'form': form})

def lista_alumnos(request):
    """
    Muestra la tabla de alumnos registrados, útil para el control administrativo.
    """
    alumnos = Alumno.objects.all()
    return render(request, 'Usuarios/lista_alumnos.html', {'alumnos': alumnos})

@login_required
def redireccion_rol(request):
    """
    Esta vista intercepta el login. 
    Verifica el rol del usuario y lo redirige a su panel correspondiente.
    """
    # Django tiene una bandera nativa llamada 'is_staff' para detectar administradores
    if request.user.is_staff or request.user.is_superuser:
        # Es Administrativo
        return redirect('Usuarios:panel_admin')
    else:
        # Es Alumno
        return redirect('Usuarios:panel_alumno')

@login_required
def panel_admin(request):
    """Dashboard exclusivo para Administrativos."""
    # Para mayor seguridad, puedes volver a verificar aquí
    if not request.user.is_staff:
        return redirect('Usuarios:panel_alumno')
        
    return render(request, 'Usuarios/panel_admin.html')

@login_required
def panel_alumno(request):
    """Dashboard exclusivo para Alumnos."""
    # Aquí en el futuro buscaremos los datos del alumno conectado
    return render(request, 'Usuarios/panel_alumno.html')