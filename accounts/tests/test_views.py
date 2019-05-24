from django.test import Client, TestCase
from django.urls import reverse

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

