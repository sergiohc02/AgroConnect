# core/models.py
from django.db import models

class RegistroNacimiento(models.Model):
    id_animal = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    hora = models.TimeField()
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    peso = models.FloatField()
    raza = models.CharField(max_length=100)
    capa = models.CharField(max_length=100)

    def __str__(self):
        return f"Registro de Nacimiento: {self.id_animal}"
