from django.test import TestCase, Client
from django.urls import reverse

from model_mommy import mommy

from catalogo.models import Categoria,Servico


class ServicosTestCase(TestCase):

    def setUp(self) -> None:
        self.url = reverse('catalogo:servicos')
        self.servicos = mommy.make('catalogo.Servico', _quantity=10)

    def tearDown(self) -> None:
        Servico.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogo/servicos.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('servicos' in response.context)
        servicos = response.context['servicos']
        self.assertEquals(servicos.count(), 2)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 5)

    def test_page_notfound(self):
        response = self.client.get('{}?page=6'.format(self.url))
        self.assertEquals(response.status_code, 404)
