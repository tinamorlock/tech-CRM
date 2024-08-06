from django import forms

from .models import Lead, LeadNote


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'first_name',
            'last_name',
            'company',
            'email',
            'phone',
            'source',
        ]


class LeadNoteForm(forms.ModelForm):
    class Meta:
        model = LeadNote
        fields = [
            'note',
            'lead',
        ]