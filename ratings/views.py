from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Rating, Recipe
from .forms import RatingForm

# Просмотр всех оценок текущего пользователя
@login_required
def rating_list(request):
    ratings = Rating.objects.filter(user=request.user)
    return render(request, 'recipe_sharing_app/rating_list.html', {'ratings': ratings})

# Добавление или редактирование оценки для рецепта
@login_required
def rating_create_update(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    rating, created = Rating.objects.get_or_create(user=request.user, recipe=recipe)
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=recipe_id)
    else:
        form = RatingForm(instance=rating)
    return render(request, 'recipe_sharing_app/rating_form.html', {'form': form, 'recipe': recipe})

# Удаление оценки
@login_required
def rating_delete(request, rating_id):
    rating = get_object_or_404(Rating, pk=rating_id, user=request.user)
    if request.method == 'POST':
        rating.delete()
        return redirect('rating_list')
    return render(request, 'recipe_sharing_app/rating_confirm_delete.html', {'rating': rating})