# remind_me_later/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Remind-Me-Later API!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/reminder/', include('reminder.urls')),  # ✅ Only this
]
