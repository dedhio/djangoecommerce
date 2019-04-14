from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy

from catalogo.models import Categoria,Servico


class CategoriaTestCase(TestCase):

    def setUp(self):
        self.categoria = mommy.make('catalogo.Categoria')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.categoria.get_absolute_url(),
            reverse('catalogo:categoria', kwargs={'slug': self.categoria.slug})
        )


class ServicoTestCase(TestCase):

    def setUp(self) -> None:
        self.servico = mommy.make(Servico, slug='servico')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.servico.get_absolute_url(),
            reverse('catalogo:servico', kwargs={'slug': 'servico'})
        )
