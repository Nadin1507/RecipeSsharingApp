from django.contrib import admin

# Register your models here.

# from django.contrib import admin
# from django.contrib.auth.models import Group, Permission
#
# admin.site.register(Group)
# admin.site.register(Permission)

from django.contrib import admin
# from .models import Recipes


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


# admin.site.register(Recipes, RecipeAdmin)
