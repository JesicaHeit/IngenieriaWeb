from django import forms
from django.db import models
from .models import Receta, Comment

class RecetasForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('title', 'imagen','ingredients','text',)

class CommentForm(forms.ModelForm):
	author = forms.CharField(widget=forms.TextInput(attrs={'readonly': True}), max_length = 200)
	class Meta:
		model = Comment
		fields = ('author','text',)