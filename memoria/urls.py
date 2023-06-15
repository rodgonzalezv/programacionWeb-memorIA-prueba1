from django.urls import path, include
from .views import home, quienes_somos, planes, galeria, contacto, dashboard

urlpatterns = [
    path("", home, name="home"),
    path("quienes_somos", quienes_somos, name="quienes_somos"),
    path("planes", planes, name="planes"),
    path("galeria", galeria, name="galeria"),
    path("contacto", contacto, name="contacto"),
    path("dashboard", dashboard, name="dashboard"),
]