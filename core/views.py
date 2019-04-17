from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from catalogo.models import Categoria

from .forms import ContatoForm


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


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

