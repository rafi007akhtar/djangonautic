from django.db import models
import datetime

"""
* A model is a class in Python used to represent a table in a database.
* Each class / model represents one relation only.
* Models need to be "migrated" to databases.
* In order to migrate this model, we need to create a migration file - something that tracks changes to a model.
"""

class Article (models.Model):
    # The class Article inherits from models.Model (inbuilt) class.

    """
    The Article relation will have:
      title, body, url, date, author 
    of the article in its schema.
    """

    title = models.CharField(max_length = 50) # title is a character column not more than 100 characters long
    author = models.CharField(max_length = 50) # author name
    url = models.SlugField(max_length = 100) # SlugField is used for URLs of artciles
    body = models.TextField() # artcile body
    date = models.DateTimeField(auto_now_add = True) # when the article was written, assigned by the system itself while the article gets written (the user does not need to specify the time)

    # TODO: Add article thumbnail

    def __str__(self):
        # returns what should be displayed when an article object is fetched in the console
        # 'self' in Python is equivalent to 'this' in Java
        return self.title
    
    def snippet (self):
      snip = self.body[:200]
      if len(snip) < len(self.body): snip += "..."
      return snip




