from django.db import models

class Item(models.Model):
    DESTINO_CHOICES = (
        ('Cozinha Fria', 'Cozinha Fria'),
        ('Cozinha Quente', 'Cozinha Quente'),
        ('Sobremesas', 'Sobremesas'),
    )
    nome = models.CharField('Nome', max_length=100)
    tempo_preparo = models.TimeField('Tempo de Preparo')
    ativo = models.BooleanField('Ativo?', default=True)
    diario = models.BooleanField('Cardápio Diário', default=False,)
    destino = models.CharField('Cozinha Destino', max_length=14, choices=DESTINO_CHOICES)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    data_atualizacao = models.DateTimeField('Data de Atualização', auto_now=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    SITUACAO_CHOICES = (
        ('Em Preparo', 'Em Preparo'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
        ('Baixado', 'Baixado'),
        ('Atrasado', 'Atrasado'),
    )
    item = models.ForeignKey(Item, verbose_name='Item', on_delete=models.CASCADE)
    situacao = models.CharField('Situação', max_length=10, choices=SITUACAO_CHOICES, default='Em Preparo')
    quantidade = models.IntegerField('Quantidade')
    hora_pedido = models.DateTimeField('Hora do Pedido', auto_now_add=True)
    hora_situacao = models.DateTimeField('Situação Alterada', auto_now=True)
    limite_entrega = models.TimeField('Limite da Entrega', auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __int__(self):
        return self.item

class PedidoAtrasado(models.Model):
    pedido = models.ForeignKey(Pedido, verbose_name='Pedido', on_delete=models.CASCADE)
    tempo_atraso = models.TimeField('Tempo de Atraso', auto_now_add=False, blank=True, null=True)
    data_atraso = models.DateTimeField('Data', auto_now_add=True)

    class Meta:
        verbose_name = 'Pedido Atrasado'
        verbose_name_plural = 'Pedidos Atrasados'

    def __int__(self):
        return self.pedido