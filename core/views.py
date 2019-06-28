from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib import messages

from .forms import ContatoForm

from catalogo.models import Categoria

User = get_user_model()


class IndexView(ListView):

    model = Categoria
    template_name = 'index.html'
    context_object_name = 'categorias'


index = IndexView.as_view()


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    success = False
    request.session['teste'] = 'teste'
    print(request.session['teste'])
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.send_email()
        success = True
    elif request.method == 'POST':
        messages.error(request, 'Formulario invalido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contato.html', context)

