# from django.shortcuts import render
# from .models import Recipe

def recipe_list(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

from django.shortcuts import render, get_object_or_404
from .models import Recipes

def index(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def add_recipe(request):
    return render(request, 'recipes/add_recipe.html')

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

 # recipes = Recipes.objects.all().order_by(
 #        "category", "title")
 #
 #    content['ingredients'] = {}cc
 #    for recipe in recipes:
 #        ingredients = Ingredients.objects.filter(
 #            recipe=recipe.id).order_by("id")
 #        content['ingredients'][recipe.id] = ingredients
 #    content['recipes'] = recipes