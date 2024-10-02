from django.urls import path
from first_app.views import index, catalog, users, news


urlpatterns = [
    path('', index),
    path('catalog/', catalog),
    path('users/', users),
    path('news/', news),
]