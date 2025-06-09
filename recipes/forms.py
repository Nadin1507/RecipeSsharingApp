from django import forms
from .models import Recipes

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'description', 'ingredients', 'steps', 'prep_time', 'cook_time', 'servings', 'category', 'image']