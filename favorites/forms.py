from django import forms
from .models import Favorite

class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['user', 'recipe']
        # fields = [
        #     'Favorite_type',
        #     'amount',
        #     'rate',
        #     'term',
        #     'loan_type',
        #     'collateral',
        #     'comment'
        # ]