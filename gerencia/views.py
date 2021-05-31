from django.shortcuts import render, get_object_or_404, redirect
from core.models import Item
from core.forms import ItemForm

def dashboard(request):
    contexto = {
        'titulo_pagina': 'Painel Gerencial',
    }
    return render(request, 'dashboard.html', contexto)

def listar_itens(request):
    itens = Item.objects.all()
    contexto = {
        'titulo_pagina': 'Relação de Itens',
        'titulo': 'Relação de Itens Cadastrados',
        'itens': itens,
    }
    return render(request, 'itens.html', contexto)

def cadastrar_item(request):
    form = ItemForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_itens')
    contexto = {
        'titulo_pagina': 'Cadastro de Itens',
        'titulo': 'Inclusão de novo item',
        'form': form,
    }
    return render(request, 'cadastro_item.html', contexto)

def excluir_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if str(request.method) == 'POST':
        item.delete()
        return redirect('listar_itens')
    return render(request, 'itens.html')

def atualizar_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=item)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            return redirect('listar_itens')
    contexto = {
        'form': form,
        'id_item': pk,
    }
    return render(request, 'atualiza_item.html', contexto)
