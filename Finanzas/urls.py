from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_pagos, name='lista_pagos'),
]