from django.urls import path
from third_app.views import index, forum, blog


urlpatterns = [
    path('', index),
    path('forum/', forum),
    path('blog/', blog),
]