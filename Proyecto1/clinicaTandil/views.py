from django.shortcuts import render
from django.http import HttpResponse
from clinicaTandil.models import Paciente,Medico
from clinicaTandil.forms import formSetMedico, formSetPaciente
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def inicio (request):
    return render(request,"clinicaTandil/inicio.html")

@login_required
def medicos (request):
    Medicos = Medico.objects.all()
    return render(request,"clinicaTandil/medicos/medicos.html", {"Medicos":Medicos})

def pacientes (request):
    Pacientes = Paciente.objects.all()
    return render(request,"clinicaTandil/pacientes/pacientes.html",{"Pacientes":Pacientes})

def secretarias (request):
    return render(request,"clinicaTandil/secretarias/secretarias.html")

def setPacientes (request):
    Pacientes = Paciente.objects.all()
    if request.method == 'POST':
        miFormulario = formSetPaciente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            paciente = Paciente(nombre=data["nombre"],apellido=data["apellido"], email=data["email"])
            paciente.save()
            miFormulario = formSetMedico()
            return render(request, "clinicaTandil/pacientes/setPacientes.html",{"miFormulario":miFormulario,"Pacientes":Pacientes})
    else:
        miFormulario = formSetPaciente
    return render(request,"clinicaTandil/pacientes/setPacientes.html", {"Pacientes":Pacientes})

def setMedicos (request):
    Medicos = Medico.objects.all()
    #return render(request,"clinicaTandil/medicos/medicos.html", {"Medicos":Medicos})
    if request.method == 'POST':
        miFormulario = formSetMedico(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            medico = Medico(nombre=data["nombre"],apellido=data["apellido"], especialidad=data["especialidad"])
            medico.save()
            #return render(request, "clinicaTandil/inicio.html")
            miFormulario = formSetMedico()
            return render(request,"clinicaTandil/medicos/setMedicos.html",{"miFormulario":miFormulario, "Medicos":Medicos})
    else:
        miFormulario = formSetMedico()
    return render(request,"clinicaTandil/medicos/setMedicos.html",{"miFormulario":miFormulario, "Medicos":Medicos})

def getMedico (request):
    return render(request, "clinicaTandil/medicos/getMedicos.html")

def buscarMedico (request):
    if request.GET["nombre"]: 
        nombre = request.GET["nombre"]
        medicos = Medico.objects.filter(nombre = nombre)
        return render(request, "clinicaTandil/medicos/getMedicos.html", {"medicos": medicos})
    else:
        repuesta = "No se enviaron datos"

    return HttpResponse(repuesta)

def eliminarMedico(request, nombre_medico):
    medico = Medico.objects.get(nombre = nombre_medico)
    medico.delete()
    miFormulario = formSetMedico()
    Medicos = Medico.objects.all()
    return render(request,"clinicaTandil/medicos/setMedicos.html",{"miFormulario":miFormulario, "Medicos":Medicos})

def editarMedico(request, nombre_medico):
    medico = Medico.objects.get(nombre = nombre_medico)
    
    if request.method == 'POST':
        miFormulario = formSetMedico(request.POST)
        if miFormulario.is_valid:
            print(miFormulario)
            data = miFormulario.cleaned_data
            medico.nombre = data['nombre']
            medico.apellido = data['apellido']
            medico.especialidad = data['especialidad']
            medico.save()
            miFormulario = formSetMedico()
            Medicos = Medico.objects.all()
            return render(request,"clinicaTandil/medicos/setMedicos.html",{"miFormulario":miFormulario, "Medicos":Medicos})
    else:
        miFormulario = formSetMedico(initial={'nombre': medico.nombre, 'apellido': medico.apellido, 'especialidad': medico.especialidad})
    return render(request,"clinicaTandil/medicos/editarMedico.html",{"miFormulario":miFormulario})

def loginClinica(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return render(request, "clinicaTandil/inicio.html")
        else:
            return render(request,"clinicaTandil/login.html",{'error': 'Usuario o contraseña incorrectos'})
        
    else:
        return render(request, 'clinicaTandil/login.html')
    
def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            userCreate.save()
            return render(request, 'clinicaTandil/login.html')
    else:
        return render(request, 'clinicaTandil/registro.html')