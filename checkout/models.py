from django.db import models


class CartItemManager(models.Manager):

    def add_item(self, cart_key, servico):
        if self.filter(cart_key=cart_key, servico=servico).exists():
            created = False
            cart_item = self.get(cart_key=cart_key, servico=servico)
            cart_item.quantidade = cart_item.quantidade + 1
            cart_item.save()
        else:
            created = True
            cart_item = CartItem.objects.create(cart_key=cart_key, servico=servico, preco=servico.preco)
        return cart_item, created


class CartItem(models.Model):

    cart_key = models.CharField('Chave do carrinho', max_length=40, db_index=True)
    servico = models.ForeignKey('catalogo.Servico', verbose_name='Servico', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField('Quantidade', default=1)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    objects = CartItemManager()

    class Meta:
        verbose_name = 'Item do carrinho'
        verbose_name_plural = 'Itens do carrinho'
        unique_together = (('cart_key', 'servico'),)

    def __str__(self):
        return '{} [{}]'.format(self.servico, self.quantidade)
