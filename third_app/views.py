from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, it is third application")
def forum(request):
    return HttpResponse("Here is your forum")
def blog(request):
    return HttpResponse("Here is your blog")