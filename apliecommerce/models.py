
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    texto = models.CharField(max_length=200)
    valor = models.DecimalField('Preço do produto', max_digits=8,decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, max_length=250)


    def __str__ (self):
        return self.nome

