from django.urls import path
from . import views

urlpatterns = [
    # path('', views.user_list, name='user_list'),
    path('register/', views.register, name='register'),
]

from django.urls import path
from . import views

# urlpatterns = [
    # path('', views.index, name='index'),
    # path('add/', views.add_user, name='add_user'),
    # path('user/<int:pk>/', views.user_detail, name='user_detail'),
# ]