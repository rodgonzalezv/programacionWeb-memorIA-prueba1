from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator
from django.contrib.auth.hashers import make_password

class Memorial(models.Model):
    id_memorial=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=250)
       

    class Meta:
        verbose_name = ("Memorial")
        verbose_name_plural = ("Memorials")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Memorial_detail", kwargs={"pk": self.pk})

class Planes(models.Model):
    id_plan=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    

    

    class Meta:
        verbose_name = ("Planes")
        verbose_name_plural = ("Planess")

    def __str__(self):  
        return self.nombre

    def get_absolute_url(self):
        return reverse("Planes_detail", kwargs={"pk": self.pk})

class Familiares(models.Model):
    OPC_NACIONALIDAD = (
        ('AR', 'Argentina'),
        ('BO', 'Bolivia'),
        ('BR', 'Brasil'),
        ('CL', 'Chile'),
        ('CO', 'Colombia'),
        ('CR', 'Costa Rica'),
        ('CU', 'Cuba'),
        ('EC', 'Ecuador'),
        ('SV', 'El Salvador'),
        ('GT', 'Guatemala'),
        ('HN', 'Honduras'),
        ('MX', 'México'),
        ('NI', 'Nicaragua'),
        ('PA', 'Panamá'),
        ('PY', 'Paraguay'),
        ('PE', 'Perú'),
        ('PR', 'Puerto Rico'),
        ('DO', 'República Dominicana'),
        ('UY', 'Uruguay'),
        ('VE', 'Venezuela'),
        ('OT','Otra')
        )
    
    id_familiar=models.AutoField(primary_key=True)
    nombre_familiar=models.CharField(max_length=100)
    apellidos_familiar=models.CharField(max_length=100)
    fecha_nacimiento=models.DateField(auto_now=False, auto_now_add=False)
    fecha_deceso=models.DateField(auto_now=False, auto_now_add=False)
    nacionalidad = models.CharField(max_length=2, choices=OPC_NACIONALIDAD, default='CL')
    rut_familiar=models.CharField(max_length=8, validators=[MaxLengthValidator(8)], null=False, default=12345678)
    dv_familiar=models.CharField(max_length=1, validators=[MaxLengthValidator(1)], null=False, default=0)
    

    def __str__(self):
        return self.nombre_familiar, self.apellidos_familiar

class Roles(models.Model):
    id_rol=models.AutoField(primary_key=True)
    nombre_rol=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_rol

class Recuerdos(models.Model):
    id_recuerdo=models.AutoField(primary_key=True)
    nombre_recuerdo=models.CharField(max_length=100, default='Nombre Recuerdo')
    descripcion_recuerdo=models.TextField()

    def __str__(self):
        return self.nombre_recuerdo

class Usuarios(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email=models.EmailField()
    contraseña = models.CharField(max_length=128)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    
    def set_password(self, raw_password):
        self.contraseña = make_password(raw_password)

    def __str__(self):
        return self.nombres, self.apellidos

class Usuarios_Planes(models.Model):
    id_plan_usuario=models.AutoField(primary_key=True)
    id_plan=models.ForeignKey(Planes, on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return f"Usuarios_Planes {self.fk}"
