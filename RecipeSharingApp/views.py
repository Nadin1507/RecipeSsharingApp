from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from recipes.models import Recipes
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def accounts_home(request):
    return render(request, 'accounts/index.html')  # создайте шаблон

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def recipe_list(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

@login_required
def home_view(request):
     return render(request, 'home.html')

from django.contrib.auth.decorators import permission_required

@permission_required('myapp.view_special_page')
def special_page_view(request):
    return render(request, 'special_page.html')