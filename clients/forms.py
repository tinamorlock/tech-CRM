from django import forms

from .models import Client, Contact, Site


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'company',
            'industry',
            'hourly_rate',
            'contact',
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'job_title',
            'email',
            'office_phone',
            'cell_phone',
            'home_phone',
            'company',
        ]


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = [
            'site_name',
            'address',
            'city',
            'state',
            'zip_code',
            'client',
        ]