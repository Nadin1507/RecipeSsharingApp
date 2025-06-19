from django.db import models

class Recipes(models.Model):
    title = models.TextField(db_column='Title', null=False)
    description = models.TextField()
    ingredients = models.TextField(help_text="Введите список ингредиентов")
    instructions = models.TextField(help_text="Введите шаги приготовления")
    author = models.CharField(max_length=100)
    prep_time = models.IntegerField(help_text="Время подготовки в минутах")
    cook_time = models.IntegerField(help_text="Время готовки в минутах")
    servings = models.IntegerField(help_text="Количество порций")
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)


    def __str__(self):
        return f"{self.id} - {self.title}"

