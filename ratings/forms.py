from django import forms
from .models import Rating
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('from_user', 'dtobject',
                   'shared_object')

