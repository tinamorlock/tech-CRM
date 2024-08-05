from django.urls import path, include

from .views import index

urlpatterns = [
    path('support/', index, name='support-home'),
]