from django import forms
from django.shortcuts import render , redirect
from firstApp.forms import TicketForm
from firstApp.models import Ticket
from django.contrib.auth.decorators import login_required


# Create your views here.

def templateBase(request):
    return render(request, '0_base.html')

def PaginaInicio(request):
    return render(request, '1_PaginaInicio.html')

@login_required
def crud(request):  
    tickets = Ticket.objects.all()
    data = {'tickets': tickets}
    return render(request, '4_Crud.html', data)
@login_required
def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = TicketForm()
    return render(request, '5_formCrear.html', {'form': form, 'form_open': True})

@login_required
def actualizar_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    form = TicketForm(instance=ticket)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
        return redirect('crud')

    data = {'form': form}
    return render(request, '6_formActualizar.html', data)

@login_required
def eliminar_ticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return redirect('crud')