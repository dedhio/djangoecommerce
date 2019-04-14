from django.shortcuts import render

from catalogo.models import Categoria


def index(request):
    context = {'categorias': Categoria.objects.all()}
    return render(request, 'index.html', context)


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')

