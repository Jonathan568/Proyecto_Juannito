from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_libros, name='lista_libros'),
]