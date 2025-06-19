from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['recipe', 'user', 'text', ]


# **Comment (Комментарий)**:
#    - user (ForeignKey к User)
#    - recipe (ForeignKey к Recipe)
#    - text (текст комментария)
#    - created_at(создано)
