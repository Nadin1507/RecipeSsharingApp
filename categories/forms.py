from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category', 'slug']
        widgets = {'slug': forms.HiddenInput(),
                   'category': forms.TextInput(attrs={'class': 'form-control'})}

    ...  # тут clean-методы, не относящиеся к вопросу

