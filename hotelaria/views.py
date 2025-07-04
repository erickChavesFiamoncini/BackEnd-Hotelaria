from django.shortcuts import render
from rest_framework import viewsets

from hotelaria.models import Funcionario, tipoFuncionario, Servico, tipoQuarto, Quarto

from hotelaria.serializers import quartoSerializer, tipoQuartoSerializer, funcionarioSerializer, tipoFuncionarioSerializer, servicoSerializer 

class QuartoViewSet(viewsets.ModelViewSet): 
    queryset=Quarto.objects.all()
    serializer_class=quartoSerializer

class tipoQuartoViewSet(viewsets.ModelViewSet): 
    queryset=tipoQuarto.objects.all()
    serializer_class=tipoQuartoSerializer

class FuncionarioViewSet(viewsets.ModelViewSet): 
    queryset=Funcionario.objects.all()
    serializer_class=funcionarioSerializer

class tipoFuncionarioViewSet(viewsets.ModelViewSet): 
    queryset=tipoFuncionario.objects.all()
    serializer_class=tipoFuncionarioSerializer

class ServicoViewSet(viewsets.ModelViewSet): 
    queryset=Servico.objects.all()
    serializer_class=servicoSerializer