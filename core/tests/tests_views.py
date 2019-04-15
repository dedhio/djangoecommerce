
from django.test import TestCase, Client
from django.urls import reverse
from django.core import mail


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
