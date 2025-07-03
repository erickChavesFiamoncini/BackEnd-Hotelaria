from django.contrib import admin
from .models import Hospede, reserva, pagamento

# Register your models here.
admin.site.register(Hospede)
admin.site.register(reserva)
admin.site.register(pagamento)