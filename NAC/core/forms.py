from ast import Return
from django import forms
from .models import ListaModels


class ListaForm(forms.ModelForm):
    class Meta:
        model = ListaModels
        fields = ['data','aluno', 'professor','materia']
        
   


