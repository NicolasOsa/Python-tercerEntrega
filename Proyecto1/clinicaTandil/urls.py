from django.urls import path
from clinicaTandil.views import inicio, medicos, pacientes, secretarias, setPacientes, setMedicos

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('medico/', medicos, name="Medicos"),
    path('paciente/', pacientes, name="Pacientes"),
    path('secretaria/', secretarias, name="Secretarias"),
    path('setPaciente/', setPacientes, name="setPacientes"),
    path('setMedico/', setMedicos, name="setMedicos"),
]
