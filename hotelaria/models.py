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

class tipoQuarto(models.Model):
    descricao = models.CharField(max_length=90)

    def __str__(self):
        return f'{self.descricao}'

class Quarto(models.Model):
    numero = models.IntegerField()
    andar = models.IntegerField()
    status = models.CharField(max_length=45)
    valor = models.DecimalField(decimal_places=2, max_digits=6)
    descricao = models.CharField(max_length=90)
    tipo = models.ForeignKey(tipoQuarto, on_delete=models.PROTECT, related_name='quartos', null=True, blank=True)

    def __str__(self):
        return f'{self.numero}'

