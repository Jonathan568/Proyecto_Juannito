from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin-django/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')), 
    
    path('usuarios/', include('Usuarios.urls')),
    path('biblioteca/', include('Biblioteca.urls')),
    path('finanzas/', include('Finanzas.urls')),
    
    path('', views.inicio, name='inicio'), 
]