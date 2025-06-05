from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_category, name='add_category'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]