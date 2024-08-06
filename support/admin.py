from django.contrib import admin

from .models import Ticket, TicketUpdate, Technician

admin.site.register(Ticket)
admin.site.register(TicketUpdate)
admin.site.register(Technician)
