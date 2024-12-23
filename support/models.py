from django.db import models

from clients.models import Client, Contact, Site


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ticket_client', null=True, blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='ticket_contact', null=True, blank=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='ticket_site', null=True, blank=True)


    def __str__(self):
        if self.is_resolved:
            return f'{self.title} — {self.client.company} — Resolved: {self.updated_at}'
        return f'{self.title} — {self.client.company} — Entered: {self.created_at}'
    

class TicketUpdate(models.Model):
    update = models.TextField()
    tech = models.ForeignKey('Technician', on_delete=models.CASCADE, related_name='ticket_tech', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticket_update', null=True, blank=True)


    def __str__(self):
        return f'{self.ticket.title} — Updated by {self.tech.first_name} {self.tech.last_name}'
    

class Technician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Tech: {self.first_name} {self.last_name}'