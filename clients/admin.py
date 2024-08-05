from django.contrib import admin

from .models import Client, Contact, Site

admin.site.register(Client)
admin.site.register(Contact)
admin.site.register(Site)