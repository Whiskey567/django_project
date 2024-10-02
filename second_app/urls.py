from django.urls import path
from second_app.views import index, contact, about

urlpatterns = [
    path('', index),
    path('contact', contact),
    path('about', about),
]