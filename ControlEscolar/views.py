from django.shortcuts import render
from .models import PeriodoEscolar

def lista_periodos(request):
    periodos = PeriodoEscolar.objects.all()
    return render(request, 'escolar/lista.html', {'periodos': periodos})