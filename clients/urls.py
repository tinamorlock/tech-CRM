from django.urls import path

from .views import index, create_client, create_contact, create_site 
from .views import client_detail, contact_detail, site_detail
from .views import update_client, update_contact, update_site
from .views import delete_client, delete_contact, delete_site
from .views import contact_index, site_index

urlpatterns = [
    path('clients/', index, name='clients-home'),
    path('clients/contacts/', contact_index, name='contacts-home'),
    path('clients/sites/', site_index, name='sites-home'),
    path('clients/create/client/', create_client, name='create-client'),
    path('clients/create/contact/', create_contact, name='create-contact'),
    path('clients/create/site/', create_site, name='create-site'),
    path('clients/detail/<int:pk>/', client_detail, name='client-detail'),
    path('clients/detail/contact/<int:pk>/', contact_detail, name='contact-detail'),
    path('clients/detail/site/<int:pk>/', site_detail, name='site-detail'),
    path('clients/update/client/<int:pk>/', update_client, name='update-client'),
    path('clients/update/contact/<int:pk>/', update_contact, name='update-contact'),
    path('clients/update/site/<int:pk>/', update_site, name='update-site'),
    path('clients/delete/client/<int:pk>/', delete_client, name='delete-client'),
    path('clients/delete/contact/<int:pk>/', delete_contact, name='delete-contact'),
    path('clients/delete/site/<int:pk>/', delete_site, name='delete-site'),
]