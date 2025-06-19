"""
URL configuration for RecipeSharingApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# urlpatterns = [
#   path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include

from django.urls import path
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf import settings
from django.conf.urls.static import static

from . import views

# urlpatterns = [
#     path('', views.index, name='login'),# при обращении к адресу ''(главная страница), будем использовать представление (термин Django) log
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('recipes', include('recipes.urls')),
    path('', include('categories.urls')),
    path('', include('comments.urls')),
    path('', include('favorites.urls')),
    path('', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

# urlpatterns = [
    # path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'),
#     path('logout/', views.logout_view, name='logout'),
#     path('', views.home_view, name='home'),
#     path('special/', views.special_page_view, name='special_page'),
# ]




