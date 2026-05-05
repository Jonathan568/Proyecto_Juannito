from django.contrib import admin
from django.urls import path, include
from .views import inicio

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    path('', inicio, name='inicio'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('usuarios/', include('Usuarios.urls')),
]