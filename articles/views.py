from django.shortcuts import render
from .models import Article # from models.py module in the same folder, import the Article class

def article_list (request):
    # obtain all the instances of the Article class, and order them by their 'date' attributes (newest first)
    articles = Article.objects.all().order_by('date')

    # create a dictionary with a key whose value is this collection of objects
    dici = {"arts": articles}

    # allow this dictionary to be accessible to articles.html so that articles.html can use the articles and render them on the webpage
    return render(request, "articles/articles.html", dici)