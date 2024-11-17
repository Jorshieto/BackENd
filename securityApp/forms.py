from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from firstApp.models import Ticket
import re
import unicodedata

class Ticketsoporte(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['estado', 'retroalimentacion_soporte']
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'retroalimentacion_soporte': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        
        }
        # Personaliza los campos del formulario:
        # - 'estado' como <select> con clase 'form-control'.
        # - 'retroalimentacion_soporte' como <textarea> con clase 'form-control' y 3 filas.
        # Aplica estilo Bootstrap a los campos.

# -------- Formularios para loginApp --------

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

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '').strip()
        if not re.match(r'^[A-Za-z\s]+$', first_name):
            raise ValidationError("El nombre solo puede contener letras.")
        return first_name.capitalize()

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '').strip()
        if not re.match(r'^[A-Za-z\s]+$', last_name):
            raise ValidationError("El apellido solo puede contener letras.")
        return last_name.capitalize()  

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está registrado.")
        return email

# -------- Formularios para firstApp --------


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__' # nos incluye todos los campos del modelo Ticket en el formulario
    
    def __init__(self, *args, **kwargs):
        # Llama al constructor del formulario y le aplica la clase 'form-control' a cada campo para estilos de Bootstrap
        super(TicketForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre').strip() # Quita espacios en blanco al inicio y al final
        nombre = unicodedata.normalize('NFD', nombre).encode('ascii', 'ignore').decode('utf-8')# Remover tildes
        nombre = nombre.replace('ñ', 'n') # Reemplazar 'ñ' por 'n'
        if len(nombre) > 50:
            raise forms.ValidationError("El largo máximo del nombre es 50 caracteres.")
        if not re.match(r'^[A-Za-z\s]+$', nombre):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
        if nombre == 'perrito guaton':
            raise forms.ValidationError(f"No puede ingresar el nombre: {nombre}")  # el que no debe ser nombrado
        return nombre

    def clean_fono(self):
        fono = self.cleaned_data.get('fono').strip()# Quitar espacios en blanco al inicio y al final
        if not fono.isdigit() or len(fono) != 9: # Validar que sea numérico y de 9 dígitos
            raise forms.ValidationError("El teléfono debe contener 9 dígitos numéricos.")
        return fono

    def clean_email(self):
        email = self.cleaned_data.get('email').strip()
        if '@' not in email or '.' not in email.split('@')[-1]:  #formato básico de correo
            raise forms.ValidationError("El correo debe tener un formato válido (ejemplo@dominio.cl).")
        return email

