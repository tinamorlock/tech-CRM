from django.urls import path, include

from .views import index, tech_index, ticket_update_index
from .views import create_ticket, add_update, add_tech
from .views import view_ticket, view_update, view_tech
from .views import update_ticket, update_update, update_tech
from .views import delete_ticket, delete_update, delete_tech
from .views import mark_resolved

urlpatterns = [
    path('support/', index, name='support-home'),
    path('support/techs/', tech_index, name='techs-home'),
    path('support/updates/', ticket_update_index, name='updates-home'),
    path('support/create/', create_ticket, name='create-ticket'),
    path('support/update/', add_update, name='add-update'),
    path('support/tech/', add_tech, name='add-tech'),
    path('support/ticket/<int:pk>/', view_ticket, name='view-ticket'),
    path('support/update/<int:pk>/', view_update, name='view-update'),
    path('support/tech/<int:pk>/', view_tech, name='view-tech'),
    path('support/ticket/update/<int:pk>/', update_ticket, name='update-ticket'),
    path('support/update/update/<int:pk>/', update_update, name='update-update'),
    path('support/tech/update/<int:pk>/', update_tech, name='update-tech'),
    path('support/ticket/delete/<int:pk>/', delete_ticket, name='delete-ticket'),
    path('support/update/delete/<int:pk>/', delete_update, name='delete-update'),
    path('support/tech/delete/<int:pk>/', delete_tech, name='delete-tech'),
    path('support/ticket/resolve/<int:pk>/', mark_resolved, name='ticket-resolved'),
]