from django.db import models
from django.conf import settings

# Create your models here.
class familiar(models.Model):
    parentezco_choices = (
        ('MA','Madre'),
        ('PA','Padre'),
        ('AB','Abuel@'),
        ('HE','Herman@'),
    )

    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField()
    parentezco = models.CharField(max_length=2, choices=parentezco_choices)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' '  + self.apellidos

class plan(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField(verbose_name='Cantidad Familiares')

    def __str__(self):
        return self.nombre + ' $' + str(self.precio)


class plan_cliente(models.Model):
    plan = models.ForeignKey(plan, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.plan.nombre