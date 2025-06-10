from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_list, name='favorite_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('add/', views.add_favorite, name='add_favorite'),
    # path('favorite/<int:pk>/', views.favorite_detail, name='favorite_detail'),
]