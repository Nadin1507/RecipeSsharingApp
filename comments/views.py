from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, Recipe
from .forms import CommentForm

# Просмотр всех комментариев (можно ограничить по рецепту)
def comment_list(request, recipe_id=None):
    if recipe_id:
        comments = Comment.objects.filter(recipe__id=recipe_id)
    else:
        comments = Comment.objects.all()
    return render(request, 'recipe_sharing_app/comment_list.html', {'comments': comments})

# Просмотр конкретного комментария
def comment_detail(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'recipe_sharing_app/comment_detail.html', {'comment': comment})

# Создание нового комментария
def comment_create(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user  # предполагая, что есть авторизация
            comment.save()
            return redirect('recipe_detail', pk=recipe_id)
    else:
        form = CommentForm()
    return render(request, 'recipe_sharing_app/comment_form.html', {'form': form})

# Редактирование комментария
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'recipe_sharing_app/comment_form.html', {'form': form})

# Удаление комментария
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        recipe_id = comment.recipe.id
        comment.delete()
        return redirect('recipe_detail', pk=recipe_id)
    return render(request, 'recipe_sharing_app/comment_confirm_delete.html', {'comment': comment})