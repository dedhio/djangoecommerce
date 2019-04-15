from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContatoForm(forms.Form):

    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        mensagem = self.cleaned_data['mensagem']
        mensagem = 'Nome: {0}\nEmail:{1}\n{2}'.format(nome, email, mensagem)
        send_mail('Contato Django Ecommerce', mensagem, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

