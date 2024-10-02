from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django")
def catalog(request):
    return HttpResponse("Here is catalog")
def users(request):
    return HttpResponse("Here is users")