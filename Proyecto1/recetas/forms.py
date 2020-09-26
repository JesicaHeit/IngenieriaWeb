from django import forms
from .models import Receta, Comment

class RecetasForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('title', 'ingredients','text',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)