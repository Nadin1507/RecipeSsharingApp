from django.shortcuts import render, get_object_or_404
from .models import Recipes

# Отображение списка рецептов (`recipe_list`)
def recipe_list(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

# Детальное отображение рецепта (`recipe_detail`)
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipes, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

# Добавление нового рецепта (`recipe_create`)
# @login_required
# def recipe_create(request):
#     if request.method == 'POST':
#         form = RecipesForm(request.POST)
#         if form.is_valid():
#             recipe = form.save(commit=False)
#             recipe.author = request.user
#             recipe.save()
#             form.save_m2m()
#             return redirect('recipe_detail', pk=recipe.pk)
#     else:
#         form = RecipeForm()
#     return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Добавить рецепт'})

# Редактирование рецепта (`recipe_edit`)**
#
# @login_required
# def recipe_edit(request, pk):
#     recipe = get_object_or_404(Recipe, pk=pk)
#     if request.user != recipe.author:
#         return redirect('recipe_detail', pk=pk)  # или вернуть ошибку
#     if request.method == 'POST':
#         form = RecipeForm(request.POST, instance=recipe)
#         if form.is_valid():
#             form.save()
#             return redirect('recipe_detail', pk=recipe.pk)
#     else:
#         form = RecipeForm(instance=recipe)
#     return render(request, 'recipes/recipe_form.html', {'form': form, 'title': 'Редактировать рецепт'})


def index(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})

def add_recipe(request):
    return render(request, 'recipes/add_recipe.html')

# Детальное отображение рецепта (`recipe_detail`)
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