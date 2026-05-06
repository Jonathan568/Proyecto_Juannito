from django.shortcuts import render
from .models import Libro
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_admin(request):
    return render(request, 'biblioteca/admin/dashboard_admin_biblioteca.html')

@login_required
def dashboard_alumno(request):
    return render(request, 'biblioteca/alumno/dashboard_alumno_biblioteca.html')

