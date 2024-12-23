from django.db import models

from clients.models import Client, Contact


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    invoice_date = models.DateField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_invoice', null=True, blank=True)

    def __str__(self):
        return f'{self.invoice_number} — {self.client.company} — Due: {self.due_date}'
    

class LineItem(models.Model):
    description = models.CharField(max_length=100)
    eq_or_supplies_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_hourly = models.BooleanField(default=False)
    hourly_rate = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_hourly_rate', null=True, blank=True)
    num_hours = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='monthly_invoice', null=True, blank=True)


    def __str__(self):
        return f'{self.description} — {self.invoice.invoice_number} for {self.invoice.client.company}'
    

class Payment(models.Model):
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_payment', null=True, blank=True)
    
    def __str__(self):
        return f'${self.payment_amount} on {self.payment_date} for {self.client.company}'