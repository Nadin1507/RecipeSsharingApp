from django.http import JsonResponse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from recipes.models import Recipes


# from .models import Recipes

class RecipeTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.recipe = Recipe.objects.create(
            title='Мороженое',
            description='Описание',
            ingredients='Молоко, сахар',
            instructions='Как сделать',
            author=self.user
        )

    def test_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мороженое')

    def test_recipe_detail(self):
        response = self.client.get(f'/recipe/{self.recipe.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мороженое')

    def test_create_recipe(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post('/recipe/add/', {
            'title': 'Торт',
            'description': 'Описание торта',
            'ingredients': 'мука, сахар',
            'instructions': 'Запекать',
        })
        self.assertEqual(response.status_code, 302)  # редирект после создания
        self.assertTrue(Recipes.objects.filter(title='Торт').exists())

def ping(request):
    return JsonResponse({"message": "pong"})