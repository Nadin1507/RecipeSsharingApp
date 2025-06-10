from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('add/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>/', views.comment_detail, name='comment_detail'),
]