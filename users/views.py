from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import EmailAuthenticationForm



def email_login(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                # сравниваем пароль
                if user.check_password(password):
                    login(request, user)
                    return redirect('home')  # перенаправление после входа
                else:
                    messages.error(request, 'Неверный пароль.')
            except User.DoesNotExist:
                messages.error(request, 'Пользователь с таким email не найден.')
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})










def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('login')  # Название вашего url для входа
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# # Просмотр списка всех пользователей
# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'users/user_list.html', {'users': users})
#
# # Просмотр деталей конкретного пользователя
# def user_detail(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     return render(request, 'users/user_detail.html', {'user': user})
#
# # Создание нового пользователя
# def user_create(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user_list')
#     else:
#         form = UserForm()
#     return render(request, 'users/user_form.html', {'form': form})
#
# # Редактирование существующего пользователя
# def user_update(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('user_detail', pk=pk)
#     else:
#         form = UserForm(instance=user)
#     return render(request, 'users/user_form.html', {'form': form})
#
# # Удаление пользователя
# def user_delete(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('user_list')
#     return render(request, 'users/user_confirm_delete.html', {'user': user})