from django.urls import path
from . import views

app_name = 'Finanzas'

urlpatterns = [

    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('alumno/dashboard/', views.dashboard_alumno, name='dashboard_alumno'),
    path('admin/nuevo-cargo/', views.nuevo_cargo, name='nuevo_cargo'),
    path('admin/historial/', views.historial_cargos, name='historial_cargos'),
    path('alumno/generar-ficha/', views.generar_ficha, name='generar_ficha'),
]