from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipes

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_recipes', verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='favorited_by', verbose_name='Рецепт')
    # added_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
