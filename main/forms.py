from django import forms
from .models import Recipe


# customization of the recipe forms
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'dish_name', 'author', 'image', 'description', 'ingredients', 'body')

        widgets = {
            'dish_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'margin-bottom': '20px'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
