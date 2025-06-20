# class Recipes(models.Model):
#     id = models.IntegerField(primary_key=True)
#     recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ingredients')
#     ingredient = models.CharField(max_length=128)
#
#     class Meta:
#         managed = False
#         db_table = 'ingredients'
#         verbose_name_plural = 'Ingredients'
#
#     def __str__(self):
#         return f"{self.id} {self.recipe} - {self.ingredient}"


from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    category = models.TextField(db_column='Category', null=False)
    title = models.TextField(db_column='Title', null=False)
    # submitted_by = models.TextField(db_column='Submitted_By', null=False)
    # origin = models.TextField(db_column='Origin', null=False)
    # directions = models.TextField(db_column='Directions', null=False)
    # comments = models.ForeignKey('comments.Comment', on_delete=models.CASCADE, related_name='recipe')
    # created = models.DateTimeField(null=False)
    # modified = models.DateTimeField(null=True)
    # recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ingredients')


    def __str__(self):
        return f"{self.id} - {self.title}"

    # class Meta:
    #     managed = False
    #     db_table = 'recipes'
    #     verbose_name_plural = 'Recipes'

