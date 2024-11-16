from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

# Define los grupos disponibles para el usuario
GRUPO = [
    ('admin', 'ADMIN'),
    ('jefe_area', 'Jefe de Área'),
    ('soporte', 'Soporte TI'),
]

class RegistroUsuario(UserCreationForm):  # registro usuario hereda de usercreationform que es un formulario predefinido en django
    email = forms.EmailField(label='Correo Electrónico')  # Campo adicional para el correo electrónico
    grupo = forms.ChoiceField(choices=GRUPO, label='Grupo', required=True)  # Nuevo campo para seleccionar el grupo
    first_name = forms.CharField(max_length=30, label='Nombre', required=True)  # Campo para el primer nombre
    last_name = forms.CharField(max_length=30, label='Apellido', required=True)  # Campo para el apellido

    class Meta:
        model = User  # Utiliza el modelo User de Django
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'grupo']  # Añadir los campos 'first_name' y 'last_name'
        labels = {
            'username': 'Nombre de Usuario',
        }