from django.urls import path
from . import views

app_name = 'Finanzas'

urlpatterns = [

    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('alumno/dashboard/', views.dashboard_alumno, name='dashboard_alumno'),
    path('admin/nuevo-cargo/', views.nuevo_cargo, name='nuevo_cargo'),
    path('admin/historial/', views.historial_cargos, name='historial_cargos'),
    path('alumno/generar-ficha/', views.generar_ficha, name='generar_ficha'),
    path('admin/cargo/<int:idcargo>/pagar/', views.registrar_pago, name='registrar_pago'),
    path('admin/cargo/<int:idcargo>/cancelar/', views.cancelar_cargo, name='cancelar_cargo'),
    path('admin/cargo/<int:idcargo>/recibo/', views.descargar_recibo, name='descargar_recibo'),
    path('alumno/cargo/<int:idcargo>/hoja-pago/', views.descargar_hoja_pago, name='descargar_hoja_pago'),
    path('alumno/pasarela/', views.pasarela_pago, name='pasarela_pago'),
    path('alumno/procesar-pago-linea/', views.procesar_pago_linea, name='procesar_pago_linea'),
]