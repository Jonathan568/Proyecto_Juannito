from django.urls import path
from . import views

app_name = 'Biblioteca'

urlpatterns = [
    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('alumno/dashboard/', views.dashboard_alumno, name='dashboard_alumno'),
    path('gestion/', views.gestion_biblioteca, name='gestion_biblioteca'),
    path('catalogo/', views.catalogo_alumno, name='catalogo_alumno'),
    path('solicitar/<int:libro_id>/', views.solicitar_prestamo, name='solicitar_prestamo'),
    path('registrar/', views.registrar_libro, name='registrar_libro'),
    path('devolver/<int:libro_fisico_id>/', views.devolver_libro, name='devolver_libro'),
    path('eliminar/<int:libro_fisico_id>/', views.eliminar_libro, name='eliminar_libro'),
]