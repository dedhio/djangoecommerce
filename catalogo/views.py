from django.shortcuts import render
from .models import Servico, Categoria


def servicos(request):
    context = {
        'servicos': Servico.objects.all()
    }
    return render(request, 'catalogo/servicos.html', context)


def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)
    context = {
        'categoria': categoria,
        'servicos': Servico.objects.filter(categoria=categoria)
    }
    return render(request, 'catalogo/categoria.html', context)
