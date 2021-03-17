from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from main.models import Recipe, Feedback
from .forms import RecipeForm


def home(request):
    return render(request, 'home.html')


class BlogView(ListView):
    model = Recipe
    template_name = 'blog.html'
    ordering = ['-publication_date']  # sorting from newest to oldest


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_details.html'


class CreateRecipeView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'create_recipe.html'


class UpdateRecipeView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'update_recipe.html'


class DeleteRecipeView(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')


class ContactView(CreateView):
    model = Feedback
    template_name = 'contact.html'
    fields = '__all__'  # editing all of the fields
