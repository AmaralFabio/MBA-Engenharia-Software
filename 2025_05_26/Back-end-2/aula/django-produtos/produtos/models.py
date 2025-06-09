from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    estoque = models.PositiveIntegerField(default=0)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome