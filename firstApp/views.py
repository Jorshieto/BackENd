from django import forms
from django.shortcuts import render , redirect
from securityApp.forms import TicketForm ,Ticketsoporte#se llaama el fromulario del ticket desde el securityApp
from firstApp.models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def crudSoporte(request):
    return render(request,'4.1_CrudSoporte.html')

# Vistas de base
def templateBase(request):
    return render(request, '0_base.html')

def PaginaInicio(request):
    return render(request, '1_PaginaInicio.html')

# Vista para el grupo 'jefe_area'
@login_required
def crud_jefe_area(request):
    tickets = Ticket.objects.all()  # Cargar todos los tickets
    return render(request, '4.2_CrudJefeArea.html', {'tickets': tickets})

# Vista para el grupo 'soporte'
@login_required
def crud_soporte(request):
    tickets = Ticket.objects.all()  # Cargar todos los tickets
    return render(request, '4.1_CrudSoporte.html', {'tickets': tickets})

# Vista para el grupo 'admin'
@login_required
def crud(request):  
    tickets = Ticket.objects.all()  # Cargar todos los tickets
    return render(request, '4_Crud.html', {'tickets': tickets})

# Vista para crear un ticket
@login_required
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud')  # O redirigir a la vista apropiada según el grupo
    else:
        form = TicketForm()
    return render(request, '5_formCrear.html', {'form': form, 'form_open': True})

# Vista para actualizar un ticket
@login_required
def actualizar_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    form = TicketForm(instance=ticket)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
        return redirect('crud')

    return render(request, '6_formActualizar.html', {'form': form})

@login_required
def actualizar_ticket_soporte(request, id):
    ticket = Ticket.objects.get(id=id)
    form = Ticketsoporte(instance=ticket)

    if request.method == 'POST':
        form = Ticketsoporte(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('crud_soporte')  # Puedes redirigir al lugar que necesites

    return render(request, '7_formSoporte.html', {'form': form})

# Vista para eliminar un ticket
@login_required
def eliminar_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return redirect('crud')

def cerrar_sesion(request):
    logout(request)  # Cierra la sesión
    return redirect('login')  # Redirige a la página de login después de cerrar sesión
