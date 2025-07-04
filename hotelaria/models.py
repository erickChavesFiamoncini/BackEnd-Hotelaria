from django.db import models

# Create your models here.

class Hospede(models.Model):
    cpf = models.BigIntegerField(default=0)
    email = models.EmailField(max_length=150)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Servico(models.Model):
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.descricao}'

class reserva(models.Model):
    data = models.DateField(default= '')
    noites = models.IntegerField(default='')
    hospede = models.ForeignKey(Hospede, on_delete=models.PROTECT)
    servico = models.ManyToManyField(Servico, related_name="serviços", blank=True)

    def __str__(self):
        return f'Reserva de {self.hospede.nome} - {self.data} - {self.noites} noites'

class pagamento(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2, default='')
    data = models.DateField(default='')
    forma = models.CharField(max_length=20)
    reserva = models.ForeignKey(reserva, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.valor} - {self.forma} - {self.data}'


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
    reserva = models.ForeignKey(reserva, on_delete=models.PROTECT, related_name='reservas', null=True, blank=True)

    def __str__(self):
        return f'{self.numero}'


# Create your models here.
