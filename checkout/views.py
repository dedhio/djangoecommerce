from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from django.contrib import messages

from .models import CartItem

from catalogo.models import Servico


class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        servico = get_object_or_404(Servico, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(self.request.session.session_key, servico)
        if created:
            messages.success(self.request, 'Servico adicionado com sucesso')
        else:
            messages.success(self.request, 'Servico atualizado com sucesso')
        return servico.get_absolute_url()


create_cart_item = CreateCartItemView.as_view()
