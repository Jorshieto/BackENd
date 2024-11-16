from django import forms
from django.shortcuts import render , redirect
from firstApp.forms import TicketForm
from firstApp.models import Ticket


# Create your views here.

def templateBase(request):
    return render(request, '0_base.html')

def PaginaInicio(request):
    return render(request, '1_PaginaInicio.html')

def crud(request):  #es para que me muestre los tickets
    tickets = Ticket.objects.all()  # Obtiene todos los tickets de la base de datos
    data = {'tickets': tickets}  # Crea un diccionario con los tickets
    return render(request, '4_Crud.html', data)  # Renderiza el html

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)  # Captura los datos del formulario
        if form.is_valid():
            form.save()  # Guarda el formulario solo si es válido (hace la validacion en el form)
            return redirect('crud')  # Redirigir si tiene exito
    else:
        form = TicketForm()  # nos da un formulario vacío si no es una petición POST

    # Renderiza la plantilla, manteniendo el formulario abierto siempre que haya errores
    return render(request, '5_formCrear.html', {'form': form, 'form_open': True})

def actualizar_ticket(request, id):
    ticket = Ticket.objects.get(id=id)  # Obtiene el ticket por ID
    form = TicketForm(instance=ticket)  # Inicializa el formulario con los datos del ticket

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)  # Crea un formulario con los datos del ticket
        if form.is_valid():
            form.save()  # Guarda el formulario si es válido
        return redirect('crud')  # Redirigir a la lista de tickets

    data = {'form': form}  # Prepara los datos para la plantilla
    return render(request, '6_formActualizar.html', data)  



def eliminar_ticket(request,id): # lo elimine por que estaba en negrito
    ticket = Ticket.objects.get(id=id)  # Obtiene el ticket por ID
    ticket.delete()  # Elimina el ticket
    return redirect('crud')  # Redirige a la lista de tickets