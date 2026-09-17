from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Livro
from .forms import LivroForm


def inicio(request):

    total_livros = Livro.objects.count()

    disponiveis = Livro.objects.filter(
        disponivel=True
    ).count()

    indisponiveis = Livro.objects.filter(
        disponivel=False
    ).count()

    return render(
        request,
        'acervo/inicio.html',
        {
            'total_livros': total_livros,
            'disponiveis': disponiveis,
            'indisponiveis': indisponiveis,
        }
    )


def lista_livros(request):

    nome = request.GET.get('nome', '')
    tipo = request.GET.get('tipo', '')
    categoria = request.GET.get('categoria', '')

    livros = Livro.objects.all().order_by('titulo')

    if nome:
        livros = livros.filter(
            Q(titulo__icontains=nome) |
            Q(autor__icontains=nome)
        )

    if tipo:
        livros = livros.filter(
            tipo_acervo=tipo
        )

    if categoria:
        livros = livros.filter(
            categoria=categoria
        )

    return render(
        request,
        'acervo/lista.html',
        {
            'livros': livros,
            'nome': nome,
            'tipo': tipo,
            'categoria': categoria,
            'tipos': Livro.TIPO_ACERVO,
            'categorias': Livro.CATEGORIAS,
        }
    )


def novo_livro(request):

    if request.method == 'POST':

        form = LivroForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista')

    else:

        form = LivroForm()

    return render(
        request,
        'acervo/form.html',
        {
            'form': form,
            'titulo_pagina': 'Cadastrar Livro'
        }
    )


def editar_livro(request, id):

    livro = get_object_or_404(
        Livro,
        id=id
    )

    if request.method == 'POST':

        form = LivroForm(
            request.POST,
            instance=livro
        )

        if form.is_valid():

            form.save()

            return redirect('lista')

    else:

        form = LivroForm(
            instance=livro
        )

    return render(
        request,
        'acervo/form.html',
        {
            'form': form,
            'titulo_pagina': 'Editar Livro'
        }
    )


def excluir_livro(request, id):

    livro = get_object_or_404(
        Livro,
        id=id
    )

    if request.method == 'POST':

        livro.delete()

        return redirect('lista')

    return render(
        request,
        'acervo/excluir.html',
        {
            'livro': livro
        }
    )