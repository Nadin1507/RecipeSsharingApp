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


