from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.inicio,
        name='inicio'
    ),

    path(
        'livros/',
        views.lista_livros,
        name='lista'
    ),

    path(
        'livros/novo/',
        views.novo_livro,
        name='novo_livro'
    ),

    path(
        'livros/<int:id>/editar/',
        views.editar_livro,
        name='editar_livro'
    ),

    path(
        'livros/<int:id>/excluir/',
        views.excluir_livro,
        name='excluir_livro'
    ),
]