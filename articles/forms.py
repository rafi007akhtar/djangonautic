""" This file will contain all the model files we need for the website """

from django import forms
from . import models

class CreateArticle (forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.Article
        fields = ["title", "body", "thumb"]