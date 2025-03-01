from django.db import models


from django.db import models


class Dimensao(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome


class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    dimensao = models.ForeignKey(Dimensao, on_delete=models.CASCADE, related_name='localizacoes')

    def __str__(self):
        return f"{self.nome} ({self.dimensao.nome})"

    

class Personagem(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL,null=True, related_name='personagens')

    def __str__(self):
        return self.nome

    
# Create your models here.
