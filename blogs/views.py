from django.shortcuts import render
from django.http import HttpResponse #importing that class

# Create your views here.

def home(request):
    # return HttpResponse("<h1>Home Page</h1>") #this string will appear on browser
    return render(request, 'index.html')

def about(request):
    return render(request, 'index.html')

def beauty(request):
    return render(request, 'beauty.html')