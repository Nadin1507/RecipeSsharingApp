from django import forms
from .models import Rating
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('user', 'recipe',
                   'score')

 # - user (ForeignKey к User)
 #  - recipe (ForeignKey к Recipe)
 #  - score (целое число, например от 1 до 5)