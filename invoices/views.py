from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Invoice, LineItem
from clients.models import Client, Contact
from .forms import InvoiceForm, LineItemForm

def index(request): # this will list all invoices
    invoices = Invoice.objects.all()
    line_items = LineItem.objects.all()
    clients = Client.objects.all()
    context = {
        'invoices': invoices,
        'line_items': line_items,
        'clients': clients,
    }
    return render(request, 'invoices/index.html', context)


# create a new invoice


def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('add-line-item'))
    else:
        form = InvoiceForm()
    context = {
        'form': form,
    }
    return render(request, 'invoices/add_invoice.html', context)


# create a new line item


def add_line_item(request):
    if request.method == 'POST':
        form = LineItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('invoices-home'))
    else:
        form = LineItemForm()
    context = {
        'form': form,
    }
    return render(request, 'invoices/add_line_item.html', context)


# update an invoice


def update_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect(reverse('invoices-home'))
    else:
        form = InvoiceForm(instance=invoice)
    context = {
        'form': form,
        'invoice': invoice,
    }
    return render(request, 'invoices/update_invoice.html', context)


# update a line item


def update_line_item(request, line_item_id):
    line_item = get_object_or_404(LineItem, pk=line_item_id)
    if request.method == 'POST':
        form = LineItemForm(request.POST, instance=line_item)
        if form.is_valid():
            form.save()
            return redirect(reverse('invoices-home'))
    else:
        form = LineItemForm(instance=line_item)
    context = {
        'form': form,
        'line_item': line_item,
    }
    return render(request, 'invoices/update_line_item.html', context)


# invoice detail view


def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    line_items = LineItem.objects.filter(invoice=invoice)
    client = get_object_or_404(Client, id=invoice.client.id)
    total = 0.00
    for line_item in line_items:
        if line_item.eq_or_supplies_cost:
            total += float(line_item.eq_or_supplies_cost)
        else:
            total += float(line_item.hourly_rate.hourly_rate * line_item.num_hours)
    context = {
        'invoice': invoice,
        'line_items': line_items,
        'total': total,
        'client': client,
    }
    return render(request, 'invoices/invoice_detail.html', context)


# line item detail view


def line_item_detail(request, line_item_id):
    line_item = get_object_or_404(LineItem, pk=line_item_id)
    invoice = get_object_or_404(Invoice, pk=line_item.invoice.id)
    context = {
        'line_item': line_item,
        'invoice': invoice,
    }
    return render(request, 'invoices/line_item_detail.html', context)


# delete an invoice


def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        invoice.delete()
        return redirect(reverse('invoices-home'))
    context = {
        'invoice': invoice,
    }
    return render(request, 'invoices/delete_invoice.html', context)


# delete a line item


def delete_line_item(request, line_item_id):
    line_item = get_object_or_404(LineItem, pk=line_item_id)
    if request.method == 'POST':
        line_item.delete()
        return redirect(reverse('invoices-home'))
    context = {
        'line_item': line_item,
    }
    return render(request, 'invoices/delete_line_item.html', context)