from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import ListaModels
from .forms import ListaForm


def Cadastro(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            aluno = form.data['aluno']
            professor = form.data['professor']

            form.save()

        return redirect('Listar')

    else:
        form = ListaForm
        return render(request, 'index.html', {'form': form})


def Listar(request):

    presenca = []
    context = {'ListarPresenca': presenca}
    presenca = ListaModels.objects.all()

    for presenca in presenca:
        
        context['ListarPresenca'].append(presenca)

    return render(request, 'listar.html', context)
