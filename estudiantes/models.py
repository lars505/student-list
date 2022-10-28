from pyexpat import model
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    edad = models.IntegerField()
    cedula = models.CharField(max_length=17)
    correo = models.CharField(max_length=50)
    celular = models.IntegerField()

    def __str__(self):
        return self.nombre