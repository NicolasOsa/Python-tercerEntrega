from django.db import models

# Create your models here.
class Medico(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=40)

class Paciente(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    diagnosico = models.CharField(max_length=240)

class Secretaria(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)

class Turno(models.Model):
    turnoDia = models.DateField()
    turnoHora = models.DateTimeField()
    medico = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)