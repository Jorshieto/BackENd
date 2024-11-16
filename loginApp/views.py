from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import Group
from .forms import RegistroUsuario
from django.contrib.auth import logout

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')# Obtiene el nombre de usuario del formulario
        password = request.POST.get('password')# Obtiene la contraseña del formulario
        user = authenticate(request, username=username, password=password) # Intenta autenticar al usuario
        if user is not None:# Si la autenticación es exitosa
            login(request, user)# Inicia sesión al usuario
            return redirect('crud')  # Redirige a `crud` si la autenticación es correcta
        else:# Si la autenticación falla
            messages.error(request, 'Nombre de usuario o contraseña no válidos') # Muestra un mensaje de error
    return render(request, '2_Login.html')  # Renderiza la plantilla de inicio de sesión


def registro(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)#Crea una instancia del formulario con los datos del POST
        if form.is_valid():
            # Guardar el nuevo usuario
            user = form.save()
            username = form.cleaned_data.get('username')  # Obtener el nombre de usuario

            # Asignar el grupo seleccionado al usuario
            grupo_seleccionado = form.cleaned_data.get('grupo')  # Obtener el grupo del formulario
            grupo = Group.objects.get(name=grupo_seleccionado)  # Buscar el grupo en la base de datos
            user.groups.add(grupo)  # Asignar el grupo al usuario

            # Redirigir a la página de login o a donde prefieras
            return redirect(reverse('registro') + '?success=true') # Puedes cambiar esto a la URL que desees

    else:
        form = RegistroUsuario()  # Crear el formulario vacío para el registro

    return render(request, '3_registro.html', {'form': form})  # Renderizar la plantilla de registro

def cerrar_sesion(request):
    logout(request)  # Cierra la sesión
    return redirect('login')  # Redirige a la página de login después de cerrar sesión
