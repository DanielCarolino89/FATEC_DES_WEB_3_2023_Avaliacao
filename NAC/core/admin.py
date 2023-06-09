
from django.contrib import admin
from .models import ListaModels

class ListaModelsAdmin(admin.ModelAdmin):
    list_display = ('aluno','professor')
    search_fields = ('aluno','professor')

admin.site.register(ListaModels, ListaModelsAdmin)

