from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, quienes_somos, planes, galeria, contacto, dashboard, iniciar_sesion, cerrar_sesion
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("quienes_somos", quienes_somos, name="quienes_somos"),
    path("planes", planes, name="planes"),
    path("galeria", galeria, name="galeria"),
    path("contacto", contacto, name="contacto"),
    path('dashboard', dashboard, name='dashboard'),
    path('iniciar_sesion', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    
]
