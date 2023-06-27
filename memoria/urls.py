from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from . import views
from .views import home, quienes_somos, planes, galeria, contacto, userLogin, userLogout, dashboard, userRegistro, activar_cuenta, CustomChangePasswordView, dashboard_suscripcion


urlpatterns = [
    path("", home, name="home"),
    path("quienes_somos", quienes_somos, name="quienes_somos"),
    path("planes", planes, name="planes"),
    path("galeria", galeria, name="galeria"),
    path("contacto", contacto, name="contacto"),
    path("dashboard", dashboard, name="dashboard"),
    path('userLogin', userLogin, name='userLogin'),
    path('userLogout', userLogout, name='userLogout'),
    path('userRegistro', userRegistro, name='userRegistro'),
    path('activar-cuenta/<int:user_id>/', views.activar_cuenta, name='activar_cuenta'),
    path('cambiaPass/', CustomChangePasswordView.as_view(), name='cambiaPass'),
    path('cambiaPass/logout', userLogout, name='cambiaPass/logout'),
    path('perfil', views.user_profile, name='perfil'),
    path('suscripcion', views.dashboard_suscripcion, name='suscripcion'),
]