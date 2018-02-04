#from django.http import HttpResponse
from django.shortcuts import render # used for rendering templates to user requests

def index (request):
    #return HttpResponse("<h1>Welcome</h1>")
    return render(request, "index.html")

def about (request):
    #return HttpResponse("about")
    return render(request, "about.html")