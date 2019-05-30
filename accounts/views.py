from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

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


class AtualizaSenhaView(LoginRequiredMixin, FormView):

    template_name = 'accounts/update_password.html'
    success_url = reverse_lazy('accounts:minha_conta')
    form_class = PasswordChangeForm

    def get_form_kwargs(self):
        kwargs = super(AtualizaSenhaView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


minha_conta = MinhaContaView.as_view()
register = RegisterView.as_view()
atualiza_user = AtualizaUserView.as_view()
atualiza_password = AtualizaSenhaView.as_view()
