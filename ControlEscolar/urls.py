from django.urls import path
from . import views

app_name = 'ControlEscolar'

urlpatterns = [

    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('admin/grupos/', views.gestionar_grupos, name='gestionar_grupos'),
    path('admin/grupos/mover/', views.mover_alumno_grupo, name='mover_alumno_grupo'),
    path('admin/horarios/', views.gestionar_horarios, name='gestionar_horarios'),
    path('admin/horarios/eliminar/<int:horario_id>/', views.eliminar_horario, name='eliminar_horario'),
    path('admin/avisos/', views.gestionar_avisos, name='gestionar_avisos'),
    path('admin/avisos/eliminar/<int:aviso_id>/', views.eliminar_aviso, name='eliminar_aviso'),
    path('mi-portal/', views.dashboard_alumno, name='dashboard_alumno'),
    path('admin/calificaciones/', views.gestionar_calificaciones, name='gestionar_calificaciones'),
    path('mi-portal/boleta/', views.boleta_alumno, name='boleta_alumno'),
]
