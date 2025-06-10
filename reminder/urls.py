# reminder/urls.py
from django.urls import path
from .views import reminder_view

urlpatterns = [
    path('', reminder_view, name='reminder-api'),  # Handles /api/reminder/
]
