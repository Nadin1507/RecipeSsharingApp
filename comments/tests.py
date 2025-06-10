from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipes, Comment

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.recipe = Recipes.objects.create(title='Test Recipe', author=self.user)
        self.comment = Comment.objects.create(content='Nice recipe', recipe=self.recipe, author=self.user)

    def test_recipe_creation(self):
        self.assertEqual(Recipes.objects.count(), 1)

    def test_comment_association(self):
        self.assertEqual(self.comment.recipe, self.recipe)
        self.assertEqual(self.comment.author, self.user)