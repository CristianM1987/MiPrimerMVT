from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)


class Vegetal(models.Model):
    nombre = models.CharField(max_length=100)
