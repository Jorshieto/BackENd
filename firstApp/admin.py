from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fono', 'email', 'area', 'servicio', 'prioridad', 'encargado')