from django.test import Client, TestCase
from django.urls import reverse
from django.conf import settings

from model_mommy import mommy

from accounts.models import User


class RegisterViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.register_url = reverse('accounts:register')

    def test_registro_ok(self):
        data = {'username': 'fulano', 'password1': 'fulano1234', 'password2': 'fulano1234', 'email': 'test@test.com'}
        response = self.client.post(self.register_url, data)
        index_url = reverse('index')
        self.assertRedirects(response, index_url)
        self.assertEquals(len(User.objects.count()), 1)

    def test_registro_error(self):
        data = {'username': 'fulano', 'password1': 'fulano1234', 'password2': 'fulano1234'}
        response = self.client.post(self.register_url, data)
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('accounts:atualiza_user')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def test_update_user_ok(self):
        data = {'name': 'test', 'email': 'test@test.com'}
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 302)
        self.client.login(username=self.user.username, password='123')
        response = self.client.post(self.url, data)
        accounts_index_url = reverse('accounts:minha_conta')
        self.assertRedirects(response, accounts_index_url)
        self.user.refresh_from_db()
        self.assertEquals(self.user.email, 'test@test.com')
        self.assertEquals(self.user.name, 'test')