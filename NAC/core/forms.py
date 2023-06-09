from django import forms
from .models import ListaModels


class ListaForm(forms.ModelForm):
    class Meta:
        model = ListaModels
        fields = ['aluno', 'professor']


