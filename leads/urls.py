from django.urls import path, include

from .views import index, lead_note_index
from .views import create_lead, create_lead_note
from .views import lead_detail, lead_note_detail
from .views import update_lead, update_lead_note
from .views import delete_lead, delete_lead_note

urlpatterns = [
    path('leads/', index, name='leads-home'),
    path('leads/notes/', lead_note_index, name='lead-notes'),
    path('leads/create/', create_lead, name='create-lead'),
    path('leads/create/note/', create_lead_note, name='create-lead-note'),
    path('leads/<int:pk>/', lead_detail, name='lead-detail'),
    path('leads/notes/<int:pk>/', lead_note_detail, name='lead-note-detail'),
    path('leads/update/<int:pk>/', update_lead, name='update-lead'),
    path('leads/notes/update/<int:pk>/', update_lead_note, name='update-lead-note'),
    path('leads/delete/<int:pk>/', delete_lead, name='delete-lead'),
    path('leads/notes/delete/<int:pk>/', delete_lead_note, name='delete-lead-note'),
]