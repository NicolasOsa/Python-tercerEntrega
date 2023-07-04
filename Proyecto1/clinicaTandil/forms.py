from django import forms

class formSetMedico(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=300)   

class formSetPaciente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    correo = forms.EmailField()