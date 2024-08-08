from django.urls import path, include

from .views import index, list_payments
from .views import add_invoice, add_line_item, add_payment
from .views import update_invoice, update_line_item, update_payment
from .views import invoice_detail, line_item_detail, view_payment
from .views import delete_invoice, delete_line_item, delete_payment
from .views import generate_pdf

urlpatterns = [
    path('invoices/', index, name='invoices-home'),
    path('invoices/payments/', list_payments, name='payments-home'),
    path('invoices/add/', add_invoice, name='add-invoice'),
    path('invoices/add_line_item/', add_line_item, name='add-line-item'),
    path('invoices/add_payment/', add_payment, name='add-payment'),
    path('invoices/detail/<int:invoice_id>/', invoice_detail, name='invoice-detail'),
    path('invoices/detail/payment/<int:payment_id>/', view_payment, name='view-payment'),
    path('invoices/detail/line_item/<int:line_item_id>/', line_item_detail, name='line-item-detail'),
    path('invoices/update/invoice/<int:invoice_id>/', update_invoice, name='update-invoice'),
    path('invoices/update/line_item/<int:line_item_id>/', update_line_item, name='update-line-item'),
    path('invoices/update/payment/<int:payment_id>/', update_payment, name='update-payment'),
    path('invoices/delete/<int:invoice_id>/', delete_invoice, name='delete-invoice'),
    path('invoices/delete/line_item/<int:line_item_id>/', delete_line_item, name='delete-line-item'),
    path('invoices/delete/payment/<int:payment_id>/', delete_payment, name='delete-payment'),
    path('invoices/pdf/<int:invoice_id>/', generate_pdf, name='generate-pdf'),
]