from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .forms import ContatoForm


User = get_user_model()


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


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

