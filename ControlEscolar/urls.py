from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_periodos, name='lista_periodos'),
]