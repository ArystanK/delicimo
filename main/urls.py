from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),  # home page
    path('blog', BlogView.as_view(), name='blog'),  # page with the list of recipes
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),  # page about concrete recipe
    path('add_recipe', CreateRecipeView.as_view(), name='create_recipe'),  # page for creating new recipe
    path('recipe/edit/<int:pk>', UpdateRecipeView.as_view(), name='update_recipe'),  # page for editing existing recipe
    path('contact/', ContactView.as_view(), name='contact'),  # page for contacts
    path('recipe/delete/<int:pk>', DeleteRecipeView.as_view(), name='delete_recipe')  # page for deletion of the recipe
]
