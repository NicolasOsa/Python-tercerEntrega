from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class formSetMedico(forms.Form):   # heredamos Form . una class generica de django que se encarga de resivir todos nuestros filts con los que va a crear un formulario
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=300)   

class formSetPaciente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    correo = forms.EmailField()

class UserEditForm(UserChangeForm):   # 
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last name"}))
    #password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] #password
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):   # 
    old_password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Old Password"}))
    new_password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "New Password"}))
    new_password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirmation new Password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2'] 
        help_texts = {k:"" for k in fields}