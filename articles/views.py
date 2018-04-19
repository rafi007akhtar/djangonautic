from django.shortcuts import render
from .models import Article # from models.py module in the same folder, import the Article class
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def article_list (request):
    # obtain all the instances of the Article class, and order them by their 'date' attributes (newest first)
    articles = Article.objects.all().order_by('date')

    # create a dictionary with a key whose value is this collection of objects
    dici = {"arts": articles}

    # allow this dictionary to be accessible to articles.html so that articles.html can use the articles and render them on the webpage
    return render(request, "articles/articles.html", dici)

def article_detail (request, slug):
    #return HttpResponse("200 OK")
    
    article = Article.objects.get(url = slug) # querying the Article relation to get its instance with its url attribute being equal to the slug parameter passed

    # create  a dictionary with a key whose value is this particular object
    dici = {"art": article}

    # allow this dictionary to be accessible to articles.html so that articles.html can use the article and render them on the webpage
    return render(request, "articles/article_detail.html", dici)

@login_required(login_url="/accounts/login/")
def article_create(request):
    # login required to add new articles
    return render(request, "articles/article_create.html")

