from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse

from decimal import Decimal as decimal

from .models import Invoice, LineItem, Payment
from clients.models import Client, Contact
from .forms import InvoiceForm, LineItemForm, PaymentForm

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



def list_payments(request):
    payments = Payment.objects.all()
    context = {
        'payments': payments,
    }
    return render(request, 'invoices/payments.html', context)


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
            client = get_object_or_404(Client, pk=form.cleaned_data['invoice'].client.id)
            add_to_balance = form.cleaned_data['eq_or_supplies_cost'] or (form.cleaned_data['hourly_rate'].hourly_rate * form.cleaned_data['num_hours'])
            client.balance = client.balance + decimal(add_to_balance)
            client.save()
            print(client.balance)
            return redirect(reverse('invoices-home'))
    else:
        form = LineItemForm()
    context = {
        'form': form,
    }
    return render(request, 'invoices/add_line_item.html', context)


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            client = get_object_or_404(Client, pk=form.cleaned_data['client'].id)
            client.balance = client.balance - form.cleaned_data['payment_amount']
            client.save()
            return redirect(reverse('payments-home'))
    else:
        form = PaymentForm()
    context = {
        'form': form,
    }
    return render(request, 'invoices/add_payment.html', context)

# update an invoice


def update_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect(reverse('invoice-detail', kwargs={'invoice_id': invoice_id}))
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
    temp_amount = line_item.eq_or_supplies_cost or (line_item.hourly_rate.hourly_rate * line_item.num_hours)
    if request.method == 'POST':
        form = LineItemForm(request.POST, instance=line_item)
        if form.is_valid():
            form.save()
            client = get_object_or_404(Client, pk=form.cleaned_data['invoice'].client.id)
            if temp_amount != (form.cleaned_data['eq_or_supplies_cost'] or (form.cleaned_data['hourly_rate'].hourly_rate * form.cleaned_data['num_hours'])):
                client.balance = client.balance - decimal(temp_amount)
                client.balance = client.balance + (form.cleaned_data['eq_or_supplies_cost'] or (form.cleaned_data['hourly_rate'].hourly_rate * form.cleaned_data['num_hours']))
                client.save()
            return redirect(reverse('line-item-detail', kwargs={'line_item_id': line_item_id}))
    else:
        form = LineItemForm(instance=line_item)
    context = {
        'form': form,
        'line_item': line_item,
    }
    return render(request, 'invoices/update_line_item.html', context)


def update_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    temp_payment = payment.payment_amount
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            client = get_object_or_404(Client, pk=form.cleaned_data['client'].id)
            # check if temp payment is not equal to the new payment amount
            if temp_payment != form.cleaned_data['payment_amount']:
                client.balance = client.balance + decimal(temp_payment)
                client.balance = client.balance - form.cleaned_data['payment_amount']
                client.save()
            return redirect(reverse('view-payment', kwargs={'payment_id': payment_id}))
    else:
        form = PaymentForm(instance=payment)
    context = {
        'form': form,
        'payment': payment,
    }
    return render(request, 'invoices/update_payment.html', context)


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


def view_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    context = {
        'payment': payment,
    }
    return render(request, 'invoices/view_payment.html', context)


# delete an invoice


def delete_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    line_items = LineItem.objects.filter(invoice=invoice)
    temp_amount = 0.00
    for line_item in line_items:
        if line_item.eq_or_supplies_cost:
            temp_amount += float(line_item.eq_or_supplies_cost)
        else:
            temp_amount += float(line_item.hourly_rate.hourly_rate * line_item.num_hours)
    if request.method == 'POST':
        client = get_object_or_404(Client, pk=invoice.client.id)
        client.balance = client.balance - decimal(temp_amount)
        invoice.delete()
        return redirect(reverse('invoices-home'))
    context = {
        'invoice': invoice,
    }
    return render(request, 'invoices/delete_invoice.html', context)


# delete a line item


def delete_line_item(request, line_item_id):
    line_item = get_object_or_404(LineItem, pk=line_item_id)
    temp_amount = line_item.eq_or_supplies_cost or (line_item.hourly_rate.hourly_rate * line_item.num_hours)
    if request.method == 'POST':
        client = get_object_or_404(Client, pk=line_item.invoice.client.id)
        client.balance = client.balance - decimal(temp_amount)
        line_item.delete()
        client.save()
        return redirect(reverse('invoices-home'))
    context = {
        'line_item': line_item,
    }
    return render(request, 'invoices/delete_line_item.html', context)


def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    if request.method == 'POST':
        client = get_object_or_404(Client, pk=payment.client.id)
        client.balance = client.balance + payment.payment_amount
        payment.delete()
        client.save()
        return redirect(reverse('payments-home'))
    context = {
        'payment': payment,
    }
    return render(request, 'invoices/delete_payment.html', context)
# generate a PDF invoice


def generate_pdf(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    line_items = LineItem.objects.filter(invoice=invoice)
    client = get_object_or_404(Client, id=invoice.client.id)
    invoice_total = 0.00
    for line_item in line_items:
        if line_item.eq_or_supplies_cost:
            invoice_total += float(line_item.eq_or_supplies_cost)
        else:
            invoice_total += float(line_item.hourly_rate.hourly_rate * line_item.num_hours)
    payments_made = 0.00
    pastdue_amt = 0.00
    if client.balance < invoice_total:
        payments_made = invoice_total - float(client.balance)
    if client.balance > invoice_total:
        pastdue_amt = client.balance - decimal(invoice_total)
    print(client.balance)
    context = {
        'invoice': invoice,
        'line_items': line_items,
        'invoice_total': invoice_total,
        'client': client,
        'grand_total': client.balance,
        'payments_made': payments_made,
        'pastdue_amt': pastdue_amt,
    }
    template_path = 'invoices/pdf_invoice.html'
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename={invoice.invoice_number}.pdf'  
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response