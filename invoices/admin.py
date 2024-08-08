from django.contrib import admin

from .models import Invoice, LineItem, Payment

admin.site.register(Invoice)
admin.site.register(LineItem)
admin.site.register(Payment)