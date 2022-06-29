from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Alumnos(models.Model):
    matricula = models.CharField(max_length=12,verbose_name="Mat")
    nombre = models.TextField()
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True, upload_to="fotos",verbose_name='Fotos')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):  # return number position model
        return self.nombre