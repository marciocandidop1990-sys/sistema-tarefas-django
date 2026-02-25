from django.shortcuts import render
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})

from .forms import TarefaForm
from django.shortcuts import redirect

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()

    return render(request, 'tarefas/criar.html', {'form': form})

from django.shortcuts import get_object_or_404

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)

    return render(request, 'tarefas/criar.html', {'form': form})

from django.shortcuts import get_object_or_404

def deletar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas')

from rest_framework import viewsets
from .serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer