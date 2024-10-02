from django.urls import path
from first_app.views import index, catalog, users


urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('users/', users),
]