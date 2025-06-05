from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite, Recipe

# Просмотр списка избранных рецептов текущего пользователя
@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'recipe_sharing_app/favorite_list.html', {'favorites': favorites})

# Добавление рецепта в избранное
@login_required
def favorite_add(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, recipe=recipe)
    return redirect('recipe_detail', pk=recipe_id)

# Удаление рецепта из избранных
@login_required
def favorite_remove(request, favorite_id):
    favorite = get_object_or_404(Favorite, pk=favorite_id, user=request.user)
    if request.method == 'POST':
        favorite.delete()
        return redirect('favorite_list')
    return render(request, 'recipe_sharing_app/favorite_confirm_delete.html', {'favorite': favorite})