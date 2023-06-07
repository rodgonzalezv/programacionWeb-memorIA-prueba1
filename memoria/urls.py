from django.urls import path, include
from .views import home, quienes_somos, planes, galeria, contacto

urlpatterns = [
    path("", home, name="home"),
    path("quienes-somos", quienes_somos, name="quienes_somos"),
    path("planes", planes, name="planes"),
    path("galeria", galeria, name="galeria"),
    path("contacto", contacto, name="contacto"),
]
