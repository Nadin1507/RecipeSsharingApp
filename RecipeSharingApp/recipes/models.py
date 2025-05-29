from django.db import models

class Recipe(models.Model): # Создаём новый класс, который будет служить для блога моделью, указывая все необходимые элементы.
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
   # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipes',
#                             verbose_name='Категория')

    def __str__(self):# С помощью функции меняем то, как будет представлена запись в модели.
        return self.title # Указываем, что она будет идентифицироваться с помощью своего заголовка.

    class Meta:
        verbose_name_plural = "Recipes"  # Указываем правильное написание для множественного числа слова Entry.


from django.contrib.auth.models import User
from django.db import models


class UserRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"


from django.db import models
from recipes.models import Recipe
from django.contrib.auth.models import User

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments', verbose_name='Рецепт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Пользователь')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Комментарий {self.user.username} к {self.recipe.title}"


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_recipes', verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='favorited_by', verbose_name='Рецепт')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')

    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные рецепты'

    def __str__(self):
        return f"{self.user.username} выбрал рецепт {self.recipe.title}"

from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings', verbose_name='Рецепт')
    score = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата оценки')

    class Meta:
        unique_together = ('user', 'recipe')
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f"{self.user.username} поставил {self.score} за {self.recipe.title}"