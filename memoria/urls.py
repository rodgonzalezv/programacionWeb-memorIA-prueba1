from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from . import views
from .views import home, quienes_somos, planes, galeria, contacto, userLogin, userLogout, dashboard_home, userRegistro, activar_cuenta, familiarRegistro, familiarListado, familiarUpdate, familiarDelete, CustomChangePasswordView, dashboard_suscripcion, pago_exitoso, queplan


urlpatterns = [
    path("", home, name="home"),
    path("quienes_somos", quienes_somos, name="quienes_somos"),
    path("planes", planes, name="planes"),
    path("galeria", galeria, name="galeria"),
    path("contacto", contacto, name="contacto"),
    path("dashboard_home", dashboard_home, name="dashboard_home"),
    path('dashboard_familiarRegistro', familiarRegistro, name='dashboard_familiarRegistro'),
    path('dashboard_familiarListado', familiarListado, name='dashboard_familiarListado'),
    path('familiarDelete/<int:familiar_id>/', familiarDelete, name='familiarDelete'),
    path('dashboard_familiarUpdate/<int:familiar_id>/', familiarUpdate, name='dashboard_familiarUpdate'),
    path('userLogin', userLogin, name='userLogin'),
    path('userLogout', userLogout, name='userLogout'),
    path('userRegistro', userRegistro, name='userRegistro'),
    path('activar-cuenta/<int:user_id>/', views.activar_cuenta, name='activar_cuenta'),
    path('cambiaPass/', CustomChangePasswordView.as_view(), name='cambiaPass'),
    path('cambiaPass/logout', userLogout, name='cambiaPass/logout'),
    path('perfil', views.user_profile, name='perfil'),
    path('dashboard_suscripcion', views.dashboard_suscripcion, name='dashboard_suscripcion'),
    path('pagoexitoso', pago_exitoso, name='pagoexitoso'),
    path('queplan/', views.queplan, name='queplan'),

]