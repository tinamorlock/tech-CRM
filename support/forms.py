from django import forms

from .models import Ticket, TicketUpdate, Technician


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'client', 'contact', 'site']



class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = TicketUpdate
        fields = ['update', 'tech', 'ticket']



class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ['first_name', 'last_name', 'email', 'phone', 'is_active']