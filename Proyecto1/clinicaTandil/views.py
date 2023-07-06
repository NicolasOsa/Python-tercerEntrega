from django.shortcuts import render, redirect
from django.http import HttpResponse
from clinicaTandil.models import Paciente,Medico, Avatar
from clinicaTandil.forms import formSetMedico, formSetPaciente, UserEditForm,ChangePasswordForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

@login_required
def inicio (request):
    avatar = getavatar(request)
    return render(request,"clinicaTandil/inicio.html", {"avatar": avatar})

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
        if userCreate.is_valid():   #  if userCreate is not None:
            userCreate.save()
            return render(request, 'clinicaTandil/login.html')
    else:
        return render(request, 'clinicaTandil/registro.html')
    


@login_required
def perfilView(request):
    return render(request, 'clinicaTandil/perfil/perfil.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'clinicaTandil/perfil/perfil.html')
    else:
        form = UserEditForm(initial= {'username': usuario.username,'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'clinicaTandil/perfil/editarPerfil.html', {"form": form})
    

def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data= request.POST, user= usuario)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
        return render(request,"clinicaTandil/inicio.html")
    else:
        form = ChangePasswordForm(user=usuario)
        return render(request, 'clinicaTandil/perfil/changePassword.html', {"form": form})
    


def editAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "clinicaTandil/inicio.html", {'avatar': avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "clinicaTandil/perfil/avatar.html", {'form': form})

def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar