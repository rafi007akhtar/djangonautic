from django.shortcuts import render, redirect
from .models import Article # from models.py module in the same folder, import the Article class
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list (request):
    # obtain all the instances of the Article class, and order them by their 'date' attributes (newest first)
    articles = Article.objects.all().order_by('date')

    # create a dictionary with a key whose value is this collection of objects
    dici = {"arts": articles, "user": request.user}

    # allow this dictionary to be accessible to articles.html so that articles.html can use the articles and render them on the webpage
    return render(request, "articles/articles.html", dici)

def article_detail (request, slug):
    #return HttpResponse("200 OK")
    
    article = Article.objects.get(url = slug) # querying the Article relation to get its instance with its url attribute being equal to the slug parameter passed

    # create  a dictionary with a key whose value is this particular object
    dici = {"art": article, "user": request.user}

    # allow this dictionary to be accessible to articles.html so that articles.html can use the article and render them on the webpage
    return render(request, "articles/article_detail.html", dici)


# login required to add new articles
@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == "POST":
        # Validate the form, save it to database, redirect to article listing page
        form = forms.CreateArticle(request.POST, request.FILES) # the second parameter is for the thumb field validation
        if form.is_valid:
            # Save it to the database
            instance = form.save(commit = False) # retrieve the validated form (without author as a field) without actually saving it to the datavase (made sure by the paramter)
            instance.author = request.user # add the author key to the form with value as the username
            instance.save() # save the form in the database
            instance.url = Article.slugGenerator(instance.title)
            instance.save()
            return redirect("articles:list")
    else: 
        form = forms.CreateArticle() 
        return render(request, "articles/article_create.html", {'form': form, "user": request.user})

