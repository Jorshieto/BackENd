from django import forms
from firstApp.models import Ticket
import re
import unicodedata

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
