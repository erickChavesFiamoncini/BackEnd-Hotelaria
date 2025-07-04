from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from hotelaria.views import QuartoViewSet, tipoQuartoViewSet, FuncionarioViewSet, tipoFuncionarioViewSet, ServicoViewSet

router = DefaultRouter()
router.register(r"quartos", QuartoViewSet)
router.register(r"tipos de quartos", tipoQuartoViewSet)
router.register(r"funcionários", FuncionarioViewSet)
router.register(r"tipos de funcionários", tipoFuncionarioViewSet)
router.register(r"serviços", ServicoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
]
