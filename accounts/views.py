from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from .forms import UserAdminCreationForm


class MinhaContaView(LoginRequiredMixin, TemplateView):

    template_name = 'accounts/minha_conta.html'


class RegisterView(CreateView):

    model = User
    template_name = 'accounts/nova_conta.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('index')


class AtualizaUserView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'accounts/update_conta.html'
    fields = ['nome', 'email']
    success_url = reverse_lazy('accounts:minha_conta')

    def get_object(self, queryset=None):
        return self.request.user


minha_conta = MinhaContaView.as_view()
register = RegisterView.as_view()
atualiza_user = AtualizaUserView.as_view()
