from rest_framework import serializers
from .models import Recipes, Ingredient, Comment
from django.contrib.auth.models import User
from django.db import models


class IngredientSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Ingredient.
    Используется для отображения и создания ингредиентов.
    """

    class Meta:
        model = Ingredient
        fields = ['name', 'quantity']


class RecipeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Recipe.
    Обеспечивает преобразование рецептов в формат JSON и наоборот.
    Включает вложенные ингредиенты и комментарии.
    """
    ingredients = IngredientSerializer(many=True)
    author = serializers.ReadOnlyField(source='author.username')  # Имя создателя рецепта

    class Meta:
        model = Recipes
        fields = ['id', 'title', 'description', 'ingredients', 'author', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Comment.
    Позволяет отображать и добавлять комментарии к рецептам.
    """
    user = serializers.ReadOnlyField(source='user.username')  # Имя пользователя, оставившего комментарий

    class Meta:
        model = Comment
        fields = ['id', 'recipe', 'user', 'content', 'created_at']
        extra_kwargs = {
            'recipe': {'write_only': True}  # чтобы при создании комментария указывался рецепт
        }

        # class CommentSerializer(serializers.ModelSerializer):
        #     class Meta:
        #         model = Comment
        #         fields = ['id', 'author', 'recipe', 'text', 'created_at']
        #         read_only_fields = ['id', 'author', 'created_at']


        class Comment(models.Model):
            author = models.ForeignKey(User, on_delete=models.CASCADE)
            recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='comments')
            text = models.TextField()
            created_at = models.DateTimeField(auto_now_add=True)