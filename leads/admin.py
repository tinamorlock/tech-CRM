from django.contrib import admin

from .models import Lead, LeadNote

admin.site.register(Lead)
admin.site.register(LeadNote)