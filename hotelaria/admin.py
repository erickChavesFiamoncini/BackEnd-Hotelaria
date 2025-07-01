from django.contrib import admin

from hotelaria.models import Funcionario
from hotelaria.models import tipoFuncionario
from hotelaria.models import Servico

admin.site.register(tipoFuncionario)
admin.site.register(Funcionario)
admin.site.register(Servico)

