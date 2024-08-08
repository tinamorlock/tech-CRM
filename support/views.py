from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta


from .models import Ticket, TicketUpdate, Technician
from .models import Client, Contact, Site

from .forms import TicketForm, TicketUpdateForm, TechnicianForm


def index(request):
    tickets = Ticket.objects.filter(is_resolved=False)
    context = {
        'tickets': tickets
    }
    return render(request, 'support/index.html', context)


def tech_index(request):
    techs = Technician.objects.all()
    context = {
        'techs': techs
    }
    return render(request, 'support/tech_index.html', context)


def ticket_update_index(request):
    now = timezone.now()
    thirty_days_ago = now - timedelta(days=30) # adjust if you want shorter or longer time frame
    updates = TicketUpdate.objects.filter(created_at__gte=thirty_days_ago).order_by('-created_at')
    context = {
        'updates': updates
    }
    return render(request, 'support/updates_index.html', context)


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('support-home')) # when detail view created, have it redirect to that view
    else:
        form = TicketForm()
    return render(request, 'support/create_ticket.html', {'form': form})


def add_update(request):
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('updates-home')) # when detail view created, have it redirect to that view
    else:
        form = TicketUpdateForm()
    return render(request, 'support/add_update.html', {'form': form})


def add_tech(request):
    if request.method == 'POST':
        form = TechnicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('techs-home')) # when detail view created, have it redirect to that view
    else:
        form = TechnicianForm()
    return render(request, 'support/add_tech.html', {'form': form})


def view_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    updates = TicketUpdate.objects.filter(ticket=ticket)
    # create a variable to the last update on the ticket
    last_update = TicketUpdate.objects.filter(ticket=ticket).order_by('-created_at').first()
    context = {
        'ticket': ticket,
        'updates': updates,
        'last_update': last_update
    }
    return render(request, 'support/view_ticket.html', context)


def view_update(request, pk):
    update = get_object_or_404(TicketUpdate, pk=pk)
    context = {
        'update': update
    }
    return render(request, 'support/view_update.html', context)


def view_tech(request, pk):
    tech = get_object_or_404(Technician, pk=pk)
    # gets last five updates this tech has made
    updates = TicketUpdate.objects.filter(tech=tech).order_by('-created_at')[:5]
    context = {
        'tech': tech,
        'updates': updates,
    }
    return render(request, 'support/view_tech.html', context)


def update_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect(reverse('view-ticket', kwargs={'pk': pk}))
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'support/update_ticket.html', {'form': form, 'ticket': ticket})


def update_update(request, pk):
    update = get_object_or_404(TicketUpdate, pk=pk)
    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect(reverse('view-update', kwargs={'pk': pk}))
    else:
        form = TicketUpdateForm(instance=update)
    return render(request, 'support/update_update.html', {'form': form, 'update': update})


def update_tech(request, pk):
    tech = get_object_or_404(Technician, pk=pk)
    if request.method == 'POST':
        form = TechnicianForm(request.POST, instance=tech)
        if form.is_valid():
            form.save()
            return redirect(reverse('view-tech', kwargs={'pk': pk}))
    else:
        form = TechnicianForm(instance=tech)
    return render(request, 'support/update_tech.html', {'form': form, 'tech': tech})


def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect(reverse('support-home'))
    return render(request, 'support/delete_ticket.html', {'ticket': ticket})


def delete_update(request, pk):
    update = get_object_or_404(TicketUpdate, pk=pk)
    if request.method == 'POST':
        update.delete()
        return redirect(reverse('updates-home'))
    return render(request, 'support/delete_update.html', {'update': update})


def delete_tech(request, pk):
    tech = get_object_or_404(Technician, pk=pk)
    if request.method == 'POST':
        tech.delete()
        return redirect(reverse('techs-home'))
    return render(request, 'support/delete_tech.html', {'tech': tech}) 


def mark_resolved(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if ticket.is_resolved:
        return redirect(reverse('view-ticket', kwargs={'pk': pk}))
    else:
        ticket.is_resolved = True
        # set tech to last tech who updated ticket
        last_update = TicketUpdate.objects.filter(ticket=ticket).order_by('-created_at').first()
        # add update that says it's resolved and assign the tech from the last_update
        TicketUpdate.objects.create(update='Ticket Resolved', tech=last_update.tech, ticket=ticket)
        ticket.save()
        return redirect(reverse('view-ticket', kwargs={'pk': pk}))