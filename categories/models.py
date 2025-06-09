from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    slug = models.SlugField(unique=True)
    # description = models.TextField(blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.category