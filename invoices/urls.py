from django.urls import path, include

from .views import index
from .views import add_invoice, add_line_item
from .views import update_invoice, update_line_item
from .views import invoice_detail, line_item_detail
from .views import delete_invoice, delete_line_item
from .views import generate_pdf

urlpatterns = [
    path('invoices/', index, name='invoices-home'),
    path('invoices/add/', add_invoice, name='add-invoice'),
    path('invoices/add_line_item/', add_line_item, name='add-line-item'),
    path('invoices/detail/<int:invoice_id>/', invoice_detail, name='invoice-detail'),
    path('invoices/detail/line_item/<int:line_item_id>/', line_item_detail, name='line-item-detail'),
    path('invoices/update/invoice/<int:invoice_id>/', update_invoice, name='update-invoice'),
    path('invoices/update/line_item/<int:line_item_id>/', update_line_item, name='update-line-item'),
    path('invoices/delete/<int:invoice_id>/', delete_invoice, name='delete-invoice'),
    path('invoices/delete/line_item/<int:line_item_id>/', delete_line_item, name='delete-line-item'),
    path('invoices/pdf/<int:invoice_id>/', generate_pdf, name='generate-pdf'),
]