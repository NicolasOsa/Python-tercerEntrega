from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inicio (request):
    return render(request,"clinicaTandil/inicio.html")

def medicos (request):
    return render(request,"clinicaTandil/medicos.html")

def pacientes (request):
    return render(request,"clinicaTandil/pacientes.html")

def secretarias (request):
    return render(request,"clinicaTandil/secretarias.html")