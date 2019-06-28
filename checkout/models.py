from django.db import models


class CartItem(models.Model):

    cart_item = models.CharField('Chave do carrinho', max_length=40, db_index=True)
    servico = models.ForeignKey('catalogo.Servico', verbose_name='Servico', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    class Meta:
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Itens do carrinho'

    def __str__(self):
        return '{} [{}]'.format(self.servico, self.quantidade)