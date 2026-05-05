from django.shortcuts import render
from .models import Pago

def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, 'finanzas/lista.html', {'pagos': pagos})