from django.urls import path
from . import views

# ESTA LÍNEA ES LA QUE FALTA:
app_name = 'Usuarios' 

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('lista/', views.lista_alumnos, name='lista_alumnos'),

    path('redireccion/', views.redireccion_rol, name='redireccion_rol'),
    path('panel-administrativo/', views.panel_admin, name='panel_admin'),
    path('mi-portal/', views.panel_alumno, name='panel_alumno'),
]
