from django.urls import path
from django.contrib.auth.views import LogoutView
from clinicaTandil.views import inicio, medicos, pacientes, secretarias, setPacientes, setMedicos, getMedico, eliminarMedico, editarMedico, loginClinica, registro, perfilView, editarPerfil,changePassword, editAvatar

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('medico/', medicos, name="Medicos"),
    path('paciente/', pacientes, name="Pacientes"),
    path('secretaria/', secretarias, name="Secretarias"),
    path('setPaciente/', setPacientes, name="setPacientes"),
    path('setMedico/', setMedicos, name="setMedicos"),
    path('getMedico/', getMedico, name="getMedico"),
    path('eliminarMedico/<nombre_medico>', eliminarMedico, name="eliminarMedico"),
    path('editarMedico/<nombre_medico>', editarMedico, name="editarMedico"),
    path('login/', loginClinica, name="login"),
    path('registro/', registro, name="registro"),
    path('Logout/', LogoutView.as_view(template_name = 'clinicaTandil/login.html'), name="Logout"),
    path('perfil/', perfilView, name="Perfil"),
    path('perfil/editarPerfil/', editarPerfil, name="editarPerfil"),
    path('perfil/changePassword/', changePassword, name="changePassword"),
    path('perfil/Avatar/', editAvatar, name="editAvatar"),
]
