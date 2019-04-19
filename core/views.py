from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, forms


from .forms import ContatoForm


class IndexView(TemplateView):

    template_name = 'index.html'


index = IndexView.as_view()


class LoginView(TemplateView):

    template_name = 'login.html'


login = LoginView.as_view()


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

