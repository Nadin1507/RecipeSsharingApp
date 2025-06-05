from django.urls import path
from . import views

urlpatterns = [
    path('', views.rating_list, name='rating_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_rating, name='add_rating'),
    path('rating/<int:pk>/', views.rating_detail, name='rating_detail'),
]