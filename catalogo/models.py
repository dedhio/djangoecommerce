
from django.db import models
from django.urls import reverse


class Categoria(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalogo:categoria', kwargs={'slug': self.slug})

class Servico(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    categoria = models.ForeignKey('catalogo.Categoria', on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=True)
    preco= models.DecimalField('Preço', decimal_places=2, max_digits=10)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['name']

    def __str__(self):
        return self.name
