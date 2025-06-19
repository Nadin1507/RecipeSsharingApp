from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm

def index(request):
    # Можно передать контекст, если нужно
    context = {
        'message': 'Добро пожаловать в раздел категорий!'
    }
    return render(request, 'recipes/index.html', context)

def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('index')  # или другая страница после добавления
    return render(request, 'categories/add_category.html')




# Просмотр всех категорий
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipe_sharing_app/category_list.html', {'categories': categories})

# Просмотр деталей конкретной категории
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'recipe_sharing_app/category_detail.html', {'category': category})

# Создание новой категории
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'recipe_sharing_app/category_form.html', {'form': form})

# Редактирование существующей категории
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'recipe_sharing_app/category_form.html', {'form': form})

# Удаление категории
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'recipe_sharing_app/category_confirm_delete.html', {'category': category})