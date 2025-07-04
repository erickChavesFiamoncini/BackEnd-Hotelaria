from django.contrib import admin
from hotelaria.models import Funcionario, tipoFuncionario, Servico, tipoQuarto, Quarto, Hospede, reserva, pagamento

admin.site.register(tipoFuncionario)
admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(tipoQuarto)
admin.site.register(Quarto)
admin.site.register(Hospede)
admin.site.register(reserva)
admin.site.register(pagamento)

