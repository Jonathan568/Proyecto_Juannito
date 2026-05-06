from django.urls import path
from . import views

app_name = 'Biblioteca'

urlpatterns = [
    path('admin/dashboard/', views.dashboard_admin, name='dashboard_admin'),
    path('alumno/dashboard/', views.dashboard_alumno, name='dashboard_alumno'),
]