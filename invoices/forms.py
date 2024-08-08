from django import forms

from .models import Invoice, LineItem, Payment


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoice_number',
            'invoice_date',
            'due_date',
            'client',
        ]


class LineItemForm(forms.ModelForm):
    class Meta:
        model = LineItem
        fields = [
            'description',
            'eq_or_supplies_cost',
            'is_hourly',
            'hourly_rate',
            'num_hours',
            'invoice',
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'payment_amount',
            'payment_date',
            'client',
        ]