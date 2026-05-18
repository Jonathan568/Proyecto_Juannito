from django.urls import path
from . import views

app_name = 'Usuarios' 

urlpatterns = [
    path('redireccion/', views.redireccion_rol, name='redireccion_rol'),
    path('panel-administrativo/', views.panel_admin, name='panel_admin'),
    path('mi-portal/', views.panel_alumno, name='panel_alumno'),
    path('redireccion/', views.redireccion_rol, name='redireccion_rol'),
    path('panel-administrativo/', views.panel_admin, name='panel_admin'),
    path('mi-portal/', views.panel_alumno, name='panel_alumno'),
    path('docker-monitor/', views.docker_panel, name='docker_panel'),
]
