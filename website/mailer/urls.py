from django.urls import path
from .views import sendMail

urlpatterns = [
    path('mail/', sendMail),
]