from django.db import models

# Create your models here.
class Soldado(models.Model):
    nome = models.CharField('Nome completo', max_length=100)
    cpf = models.IntegerField('CPF')
    categoria = models.CharField('Categoria', max_length=20)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Nome'
        verbose_name_plural = 'Nomes'

    def __str__(self):
        return self.title