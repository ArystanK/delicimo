from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Recipe(models.Model):
    description = RichTextField()  # description of the recipe (Text)
    dish_name = models.CharField(max_length=255)  # name of the recipe
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # foreign key to the user table
    body = RichTextField()  # body of the recipe
    ingredients = RichTextField()  # field in which all of the ingredients are described
    publication_date = models.DateField(auto_now_add=True)  # date when recipe was published
    image = models.ImageField(upload_to='images/')

    def __str__(self):  # toString method
        return self.dish_name + ' | ' + str(self.author)

    def get_absolute_url(self):  # define url after form completion
        return reverse('recipe_detail', args=(str(self.id)))


class Feedback(models.Model):  # model for feedback on the site
    message = RichTextField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
