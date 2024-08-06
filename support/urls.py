from django.urls import path, include

from .views import index, tech_index, ticket_update_index
from .views import create_ticket, add_update, add_tech

urlpatterns = [
    path('support/', index, name='support-home'),
    path('support/techs/', tech_index, name='techs-home'),
    path('support/updates/', ticket_update_index, name='updates-home'),
    path('support/create/', create_ticket, name='create-ticket'),
    path('support/update/', add_update, name='add-update'),
    path('support/tech/', add_tech, name='add-tech'),
]