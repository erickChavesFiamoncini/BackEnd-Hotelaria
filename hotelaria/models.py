from django.db import models

class Hospede(models.Model):
    cpf = models.BigIntegerField(default=1)
    email = models.EmailField(max_length=150)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class reserva(models.Model):
    data = models.DateField(default= '')
    noites = models.IntegerField(default='')
    hospede = models.ForeignKey(Hospede, on_delete=models.PROTECT)

    def __str__(self):
        return f'Reserva de {self.hospede.nome} - {self.data} - {self.noites} noites'

class pagamento(models.Model):
    valor = models.DecimalField(max_digits=8, decimal_places=2, default='')
    data = models.DateField(default='')
    forma = models.CharField(max_length=20)
    reserva = models.ForeignKey(reserva, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.valor} - {self.forma} - {self.data}'
    


