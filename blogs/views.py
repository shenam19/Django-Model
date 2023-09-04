from django.shortcuts import render
from django.http import HttpResponse #importing that class
from .forms import *

# Create your views here.

#ORM : Object Relational Mapping

def home(request):
    # return HttpResponse("<h1>Home Page</h1>") #this string will appear on browser
    return render(request, 'index.html')

def about(request):
    return render(request, 'index.html')

def beauty(request):
    return render(request, 'beauty.html')


#whenever HTML form uses POST method 
# we must provide CSRF Token
#

def add_blog(request):
    bform = BlogForm()
    if request.method == 'GET':
        return render(request, 'add_blog.html', {"form": bform})
    elif request.method == 'POST':
        #create a row in db

        #these 3 things are from HTML form
        b1 = Blog(title = request.POST['title'],
            content = request.POST['content'],
            picture = request.FILES['picture']
        )#will create a python object but nor row in DB

        b1.save() #this method will create a row in DB


        #this b1 is the object(a row in our table)
        # return render(request, 'add_blog.html', {"form": bform, "msg": "successfully created"})
        all_data = Blog.objects.all()

        return render(request, 'all_data.html', {'alldata' :all_data})
        
        