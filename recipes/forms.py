from django import forms
from .models import Recipes

class RecipesForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'description', 'ingredients', 'instructions', 'author', 'prep_time', 'cook_time', 'servings', 'category',
                  'image']



# Recipe (Рецепт)**:
#    - title (заголовок рецепта)
#    - description (описание)
#    - ingredients (ингредиенты — можно как текст или отдельная модель)
#    - instructions (инструкции по приготовлению)
#    - author (ForeignKey к User)
#    - prep_time,cook_time (время подготовки, время приготовления)
#    - servings (порции)
#    - category(категория)
#    - image (фото)
