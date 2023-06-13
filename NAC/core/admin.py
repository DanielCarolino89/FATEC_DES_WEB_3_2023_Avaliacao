
from django.contrib import admin
from .models import ListaModels

class ListaModelsAdmin(admin.ModelAdmin):
    list_display = ('data','aluno','professor','materia')
    search_fields = ('data','aluno','professor','materia')

admin.site.register(ListaModels, ListaModelsAdmin)

