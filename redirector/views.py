from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# You can add view functions here to handle requests and render templates.
# For example:
# def home(request):
#     return render(request, 'home.html')

def home(request):
    return render(request, 'redirector/home.html')

def about(request):
    return HttpResponse("About Page")