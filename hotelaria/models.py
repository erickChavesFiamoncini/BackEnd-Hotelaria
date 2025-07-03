from django.db import models

# Create your models here.

class Servico(models.Model):
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.descricao}'

class tipoFuncionario(models.Model):
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.descricao}'

class Funcionario(models.Model):
    nome = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    cpf = models.IntegerField()
    sexo = models.CharField(max_length=30)
    servico = models.ManyToManyField(Servico, related_name="funcionários", blank=True)
    tipo = models.ForeignKey(tipoFuncionario, on_delete=models.PROTECT, related_name='funcionários', null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'
