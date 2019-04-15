from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from catalogo.models import Categoria

from .forms import ContatoForm


def index(request):
    context = {'categorias': Categoria.objects.all()}
    return render(request, 'index.html', context)


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    success = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contato.html', context)

