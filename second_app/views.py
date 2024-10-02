from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("It is a second app")
def contact(request):
    return HttpResponse("Here is our contact form")
def about(request):
    return HttpResponse("Information about us")