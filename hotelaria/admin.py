from django.contrib import admin

from hotelaria.models import Funcionario
from hotelaria.models import tipoFuncionario
from hotelaria.models import Servico
from hotelaria.models import tipoQuarto
from hotelaria.models import Quarto

admin.site.register(tipoFuncionario)
admin.site.register(Funcionario)
admin.site.register(Servico)
admin.site.register(tipoQuarto)
admin.site.register(Quarto)


