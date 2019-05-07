
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail
from django.conf import settings

from django.contrib.auth import get_user_model

from model_mommy import mommy

User = get_user_model()

class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self) -> None:
        pass

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index.html')


class ContatoViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('contato')

    def tearDown(self) -> None:
        pass

    def test_view_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contato.html')

    def test_form_error(self):
        data = {'nome': '', 'email': '', 'mensagem': ''}
        response = self.client.post(self.url, data)
        self.assertFormError(response, 'form', 'nome', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'mensagem', 'Este campo é obrigatório.')

    def test_form_ok(self):
        data = {'nome': 'ge', 'email': 'z@x.com', 'mensagem': 'sadas asd'}
        response = self.client.post(self.url, data)
        self.assertTrue(response.context['success'])
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals(mail.outbox[0].subject, 'Contato Django Ecommerce')


class LoginViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.login_url = reverse('login')
        self.user = mommy.prepare(settings.AUTH_USER_MODEL)
        self.user.set_password('123')
        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()

    def test_login_ok(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('login.html')
        data = {'username': self.user.username, 'password': '123'}
        response = self.client.post(self.login_url, data)
        redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
        self.assertRedirects(response, redirect_url)

    def test_login_error(self):
        data = {'username': self.user.username, 'password': '1234'}
        response = self.client.post(self.login_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('login.html')
        error_msg = ('Por favor, entre com um usuário e senha corretos. '
                     'Note que ambos os campos diferenciam maiúsculas e minúsculas.')
        self.assertFormError(response, 'form', None, error_msg)


class RegisterViewTestCase(TestCase):

        def setUp(self) -> None:
            self.client = Client()
            self.login_url = reverse('nova_conta')

        def test_registro_ok(self):
            data = {'username': 'fulano', 'password1': 'fulano1234', 'password2': 'fulano1234'}
            response = self.client.post(self.login_url, data)
            redirect_url = reverse('index')
            self.assertRedirects(response, redirect_url)
            self.assertEquals(len(User.objects.count()), 1)
