from django.contrib import admin

from hotelaria.models import Funcionario, tipoFuncionario, Servico, tipoQuarto, Quarto

admin.site.register(tipoFuncionario)
admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(tipoQuarto)
admin.site.register(Quarto)


