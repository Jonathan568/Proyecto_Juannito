from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required
def redireccion_rol(request):
    if request.user.is_staff or request.user.is_superuser:
        return redirect('Usuarios:panel_admin')
    else:
        return redirect('Usuarios:panel_alumno')

@login_required
def panel_admin(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('Usuarios:panel_alumno')
    return render(request, 'Usuarios/panel_admin.html')

@login_required
def panel_alumno(request):
    return render(request, 'Usuarios/panel_alumno.html')

@user_passes_test(lambda u: u.is_superuser)
def docker_panel(request):
    return render(request, 'Usuarios/docker_panel.html')