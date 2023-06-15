from django.db import models
from django.conf import settings

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
