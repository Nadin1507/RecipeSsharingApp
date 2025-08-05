from django.db import models

# Create your models here.

from django.db import models
from recipes.models import Recipes
from django.contrib.auth.models import User

class Comment(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='comments', verbose_name='Рецепт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Пользователь')
    text = models.TextField(verbose_name='Комментарий')
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Комментарий {self.user.username} к {self.recipe.title}"

class Ingredient:
    def __init__(self, name, quantity, unit, calories_per_unit=None):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.calories_per_unit = calories_per_unit

    def total_calories(self):
        if self.calories_per_unit:
            return self.quantity * self.calories_per_unit
        return None

    def __repr__(self):
        return (f"Ingredient(name='{self.name}', "
                f"quantity={self.quantity}, unit='{self.unit}', "
                f"calories_per_unit={self.calories_per_unit})")