from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, quienes_somos, planes, galeria, contacto, login_view, dashboard
from . import views

urlpatterns = [
    path("", home, name="home"),
    path("quienes_somos", quienes_somos, name="quienes_somos"),
    path("planes", planes, name="planes"),
    path("galeria", galeria, name="galeria"),
    path("contacto", contacto, name="contacto"),
    path('login', LoginView.as_view(template_name='memoria/login.html'), name='login'),
    path('dashboard', dashboard, name='dashboard'),
]
