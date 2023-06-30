from django.shortcuts import render
from django.http import HttpResponse
from clinicaTandil.models import Paciente,Medico
from clinicaTandil.forms import formSetMedico


# Create your views here.
def inicio (request):
    return render(request,"clinicaTandil/inicio.html")

def medicos (request):
    return render(request,"clinicaTandil/medicos/medicos.html")

def pacientes (request):
    Pacientes = Paciente.objects.all()
    return render(request,"clinicaTandil/pacientes/pacientes.html",{"Pacientes":Pacientes})

def secretarias (request):
    return render(request,"clinicaTandil/secretarias/secretarias.html")

def setPacientes (request):
    if request.method == 'POST':
        paciente = Paciente(nombre=request.POST["nombre"],apellido=request.POST["apellido"], email=request.POST["email"])
        paciente.save()
        return render(request, "clinicaTandil/inicio.html")
    
    return render(request,"clinicaTandil/pacientes/setPacientes.html")

def setMedicos (request):
    if request.method == 'POST':
        miFormulario = formSetMedico(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            medico = Medico(nombre=data["nombre"],apellido=data["apellido"], especialidad=data["especialidad"])
            medico.save()
            return render(request, "clinicaTandil/inicio.html")
    else:
        miFormulario = formSetMedico()
    return render(request,"clinicaTandil/medicos/setMedicos.html",{"miFormulario":miFormulario})