from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medico(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre}, {self.apellido} - {self.especialidad}"

class Paciente(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    diagnosico = models.CharField(max_length=240)
    def __str__(self):
        return f"{self.nombre}, {self.apellido} - {self.email}"

class Secretaria(models.Model):
    nombre =models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)

class Turno(models.Model):
    turnoDia = models.DateField()
    turnoHora = models.DateTimeField()
    medico = models.CharField(max_length=40)
    paciente = models.CharField(max_length=40)

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SubCarpeta de avatares
    image = models.ImageField(upload_to='avatares', null=True, blank=True)