from django import forms
from .models import Receta

class RecetasForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('title', 'text',)