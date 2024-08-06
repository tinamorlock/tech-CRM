from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import LeadForm, LeadNoteForm

from .models import Lead, LeadNote

def index(request):
    leads = Lead.objects.all()
    context = {
        'leads': leads
    }
    return render(request, 'leads/index.html', context)


def lead_note_index(request):
    lead = Lead.objects.all()
    lead_notes = LeadNote.objects.all()
    context = {
        'lead': lead,
        'lead_notes': lead_notes
    }
    return render(request, 'leads/lead_notes.html', context)


def create_lead(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('leads-home'))
    else:
        form = LeadForm()
    return render(request, 'leads/create_lead.html', {'form': form})


def create_lead_note(request):
    if request.method == 'POST':
        form = LeadNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lead-notes'))
    else:
        form = LeadNoteForm()
    return render(request, 'leads/create_lead_note.html', {'form': form})


def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    # get all lead notes for this lead
    lead_notes = LeadNote.objects.filter(lead=lead)
    return render(request, 'leads/lead_detail.html', {'lead': lead, 'lead_notes': lead_notes})


def lead_note_detail(request, pk):
    lead_note = get_object_or_404(LeadNote, pk=pk)
    return render(request, 'leads/lead_note_detail.html', {'lead_note': lead_note})


def update_lead(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect(reverse('lead-detail', kwargs={'pk': pk}))
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads/update_lead.html', {'form': form, 'lead': lead})


def update_lead_note(request, pk):
    lead_note = get_object_or_404(LeadNote, pk=pk)
    if request.method == 'POST':
        form = LeadNoteForm(request.POST, instance=lead_note)
        if form.is_valid():
            form.save()
            return redirect(reverse('lead-note-detail', kwargs={'pk': pk}))
    else:
        form = LeadNoteForm(instance=lead_note)
    return render(request, 'leads/update_lead_note.html', {'form': form, 'lead_note': lead_note})


def delete_lead(request, pk):
    lead= get_object_or_404(Lead, pk=pk)    
    if request.method == 'POST':
        lead.delete()
        return redirect(reverse('leads-home'))
    return render(request, 'leads/delete_lead.html', {'lead': lead})


def delete_lead_note(request, pk):
    lead_note = get_object_or_404(LeadNote, pk=pk)
    if request.method == 'POST':
        lead_note.delete()
        return redirect(reverse('lead-notes'))
    return render(request, 'leads/delete_lead_note.html', {'lead_note': lead_note})