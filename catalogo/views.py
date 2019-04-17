from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Servico, Categoria


class ServicosListView(generic.ListView):

    model = Servico
    template_name = 'catalogo/servicos.html'
    context_object_name = 'servicos'
    paginate_by = 3


servicos = ServicosListView.as_view()


class CategoriaListView(generic.ListView):

    template_name = 'catalogo/categoria.html'
    context_object_name = 'servicos'
    paginate_by = 3

    def get_queryset(self):
        return Servico.objects.filter(categoria__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['categoria'] = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return context


categoria = CategoriaListView.as_view()


def servico(request, slug):
    context = {
        'servico': Servico.objects.get(slug=slug)
    }
    return render(request, 'catalogo/servico.html', context)