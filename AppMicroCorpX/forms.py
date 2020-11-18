from django import forms
import models
from django.forms import ModelForm
#Para el formulario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#Este es para el usuario común
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'rut_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Rut'
                }
            ),
            'nombre_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre'
                }
            ),
            'apellido_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Apellido Paterno'
                }
            ),
            'mail_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Dirección'
                }
            ),
            'direccion_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Correo'
                }
            ),
            'telefono_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Teléfono'
                }
            ),
            'usuario_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Correo'
                }
            ),
            'password_cli': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Contraseña'
                }
            ),
        }


#Este será para el administrador
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Usuario'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Correo'
                }
            ),
            'password1': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una Contraseña'
                }
            )
            'password2': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nuevamente la Contraseña'
                }
            )
        }
